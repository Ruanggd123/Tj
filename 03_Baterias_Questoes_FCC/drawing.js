/**
 * DrawingTool — v2.1 (Android/Mobile Fix)
 *
 * Correções para Android:
 *  - setPointerCapture no canvas: traço não "escapa" durante o desenho
 *  - touch-action: none no canvas apenas enquanto desenha
 *  - pointerout não interrompe mais o traçado (usa window para pointermove/up)
 *  - Toolbar colapsável em mobile (botão de toggle)
 *  - color-mix() substituído por cores explícitas (compatibilidade Android)
 *  - Área de toque do slider ampliada para dedo
 *  - Modo "Desenho Ativo" com badge visual e botão de saída rápida
 */
class DrawingTool {
    constructor() {
        this.currentTool  = 'cursor';
        this.isDrawing    = false;
        this.lastX        = 0;
        this.lastY        = 0;
        this.undoStack    = [];
        this.MAX_UNDO     = 20;
        this.penSize      = 4;
        this.eraserSize   = 32;
        this.isMobile     = window.matchMedia('(max-width: 768px)').matches;
        this.collapsed    = this.isMobile; // começa colapsado no mobile

        this._createCanvas();
        this._createToolbar();
        this._bindEvents();
    }

    /* ══════════════════ CANVAS ══════════════════ */
    _createCanvas() {
        this.canvas = document.createElement('canvas');
        this.canvas.id = 'drawing-canvas';
        this.ctx = this.canvas.getContext('2d');

        Object.assign(this.canvas.style, {
            position:      'fixed',
            top:           '0',
            left:          '0',
            width:         '100vw',
            height:        '100vh',
            pointerEvents: 'none',
            touchAction:   'auto', // começa sem bloquear scroll
            zIndex:        '998',
        });

        document.body.appendChild(this.canvas);
        this._resizeCanvas();
        window.addEventListener('resize', () => this._resizeCanvas(true));
    }

    _resizeCanvas(restore = false) {
        let snap;
        if (restore && this.canvas.width > 0) {
            try { snap = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height); } catch(e) {}
        }
        this.canvas.width  = window.innerWidth;
        this.canvas.height = window.innerHeight;
        if (restore && snap) this.ctx.putImageData(snap, 0, 0);
    }

    /* ══════════════════ TOOLBAR ══════════════════ */
    _createToolbar() {
        const old = document.querySelector('.drawing-toolbar, .dt2-toolbar');
        if (old) old.remove();

        this.toolbar = document.createElement('div');
        this.toolbar.className = 'dt2-toolbar';
        if (this.collapsed) this.toolbar.classList.add('dt2-collapsed');

        // Botão de toggle (hambúrguer) — visível em mobile
        this.toolbar.innerHTML = `
            <button class="dt2-toggle-btn" id="dt2-toggle" title="Ferramentas de anotação">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 000-1.41l-2.34-2.34a1 1 0 00-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
            </button>

            <div class="dt2-tools">
                <!-- Cursor -->
                <button class="dt2-btn active" data-tool="cursor" title="Cursor (Ctrl+0)">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M4 0l16 12.279-6.951 1.17 4.325 8.817-3.62 1.734-4.287-8.898-5.467 4.898z"/></svg>
                </button>

                <div class="dt2-divider"></div>

                <!-- Caneta Azul -->
                <button class="dt2-btn dt2-pen-blue" data-tool="pen-blue" title="Caneta Azul (Ctrl+1)">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 000-1.41l-2.34-2.34a1 1 0 00-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
                </button>

                <!-- Caneta Vermelha -->
                <button class="dt2-btn dt2-pen-red" data-tool="pen-red" title="Caneta Vermelha (Ctrl+2)">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 000-1.41l-2.34-2.34a1 1 0 00-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
                </button>

                <!-- Caneta Verde -->
                <button class="dt2-btn dt2-pen-green" data-tool="pen-green" title="Caneta Verde (Ctrl+3)">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 000-1.41l-2.34-2.34a1 1 0 00-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
                </button>

                <div class="dt2-divider"></div>

                <!-- Marca-texto -->
                <button class="dt2-btn dt2-highlight" data-tool="highlighter" title="Marca-texto (Ctrl+4)">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M18.5 1.15L17.35 0 10.27 7.08l1.15 1.15L8.35 11.3l-1.15-1.15L6.05 11.3l3.37 3.37 1.15-1.15-1.15-1.15 3.07-3.07 1.15 1.15L18.5 1.15zM5 19h14v2H5z"/></svg>
                </button>

                <div class="dt2-divider"></div>

                <!-- Borracha -->
                <button class="dt2-btn" data-tool="eraser" title="Borracha (Ctrl+5)">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M16.24 3.56l4.95 4.94c.78.79.78 2.05 0 2.84L12 20.53a4.008 4.008 0 01-5.66 0L2.81 17c-.78-.79-.78-2.05 0-2.84l10.6-10.6c.79-.78 2.05-.78 2.83 0zM4.22 15.58l3.54 3.53c.78.79 2.04.79 2.83 0l3.53-3.53-6.36-6.36-3.54 3.36z"/></svg>
                </button>

                <div class="dt2-divider"></div>

                <!-- Slider de tamanho -->
                <div class="dt2-size-wrap" title="Tamanho">
                    <span class="dt2-size-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="12" height="12"><circle cx="12" cy="12" r="5"/></svg>
                    </span>
                    <input type="range" class="dt2-slider" id="dt2-slider" min="1" max="40" value="4">
                    <span class="dt2-size-label" id="dt2-size-label">4px</span>
                </div>

                <div class="dt2-divider"></div>

                <!-- Desfazer -->
                <button class="dt2-btn" data-tool="undo" title="Desfazer (Ctrl+Z)">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M12.5 8c-2.65 0-5.05.99-6.9 2.6L2 7v9h9l-3.62-3.62c1.39-1.16 3.16-1.88 5.12-1.88 3.54 0 6.55 2.31 7.6 5.5l2.37-.78C21.08 11.03 17.15 8 12.5 8z"/></svg>
                </button>

                <!-- Limpar tudo -->
                <button class="dt2-btn dt2-danger" data-tool="clear" title="Limpar tudo">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M19 4h-3.5l-1-1h-5l-1 1H5v2h14V4zm-3 16H8a2 2 0 01-2-2l-1-11h14L18 18a2 2 0 01-2 2z"/></svg>
                </button>

                <!-- Preview do cursor -->
                <div class="dt2-cursor-preview" id="dt2-cursor-preview"></div>
            </div>
        `;

        document.body.appendChild(this.toolbar);
        this.sizeSlider    = this.toolbar.querySelector('#dt2-slider');
        this.sizeLabel     = this.toolbar.querySelector('#dt2-size-label');
        this.cursorPreview = this.toolbar.querySelector('#dt2-cursor-preview');
        this.toolsPanel    = this.toolbar.querySelector('.dt2-tools');
        this.toggleBtn     = this.toolbar.querySelector('#dt2-toggle');

        // Badge de "modo desenho ativo" (fita flutuante acima da toolbar no mobile)
        this.modeBadge = document.createElement('div');
        this.modeBadge.className = 'dt2-mode-badge dt2-hidden';
        this.modeBadge.innerHTML = `
            <span class="dt2-badge-dot"></span>
            <span class="dt2-badge-text">Modo Desenho</span>
            <button class="dt2-badge-close" title="Sair do modo desenho">✕</button>
        `;
        document.body.appendChild(this.modeBadge);
    }

    /* ══════════════════ EVENTOS ══════════════════ */
    _bindEvents() {
        // Toggle da toolbar (mobile)
        this.toggleBtn.addEventListener('pointerdown', e => {
            e.preventDefault();
            e.stopPropagation();
            this._toggleCollapse();
        });

        // Botão de fechar o badge de modo desenho
        this.modeBadge.querySelector('.dt2-badge-close').addEventListener('click', () => {
            this._setTool('cursor');
        });

        // Botões da toolbar
        this.toolbar.querySelectorAll('.dt2-btn[data-tool]').forEach(btn => {
            btn.addEventListener('pointerdown', e => {
                e.preventDefault();
                e.stopPropagation();
                const tool = btn.dataset.tool;
                if (tool === 'clear') { this._clearCanvas(); return; }
                if (tool === 'undo')  { this._undo(); return; }
                this._setTool(tool);
                // Em mobile: colapsa após selecionar ferramenta de desenho
                if (this.isMobile && tool !== 'cursor') {
                    setTimeout(() => this._toggleCollapse(true), 150);
                }
            });
        });

        // Slider de tamanho
        this.sizeSlider.addEventListener('input', () => {
            const v = parseInt(this.sizeSlider.value);
            this.penSize = v;
            this.sizeLabel.textContent = `${v}px`;
            this._updateCursorPreview();
        });

        // Atalhos de teclado (desktop)
        document.addEventListener('keydown', e => {
            if (e.ctrlKey || e.metaKey) {
                if (e.key === 'z' || e.key === 'Z') { e.preventDefault(); this._undo(); return; }
                const map = { '0':'cursor','1':'pen-blue','2':'pen-red','3':'pen-green','4':'highlighter','5':'eraser' };
                if (map[e.key]) { e.preventDefault(); this._setTool(map[e.key]); }
            }
            if (e.key === 'Escape') this._setTool('cursor');
        });

        /* ─── EVENTOS DE DESENHO (corrigido para Android) ───
         * Estratégia:
         *  - pointerdown no canvas: inicia traço + captura o ponteiro
         *  - pointermove no WINDOW: continua traço mesmo se sair do canvas
         *  - pointerup/cancel no WINDOW: encerra traço com segurança
         *  - pointerout NÃO encerra mais (bug mobile antigo)
         */
        this.canvas.addEventListener('pointerdown', e => this._startDraw(e));
        window.addEventListener('pointermove',  e => this._continueDraw(e), { passive: false });
        window.addEventListener('pointerup',    e => this._stopDraw(e));
        window.addEventListener('pointercancel',e => this._stopDraw(e));

        this._makeDraggable();
    }

    /* ══════════════════ TOGGLE COLLAPSE ══════════════════ */
    _toggleCollapse(forceCollapse = null) {
        if (forceCollapse === true) {
            this.collapsed = true;
        } else if (forceCollapse === false) {
            this.collapsed = false;
        } else {
            this.collapsed = !this.collapsed;
        }
        this.toolbar.classList.toggle('dt2-collapsed', this.collapsed);
    }

    /* ══════════════════ FERRAMENTAS ══════════════════ */
    _setTool(tool) {
        this.currentTool = tool;
        const isDrawingTool = tool !== 'cursor';

        // Atualiza botão ativo
        this.toolbar.querySelectorAll('.dt2-btn[data-tool]').forEach(b => b.classList.remove('active'));
        const activeBtn = this.toolbar.querySelector(`.dt2-btn[data-tool="${tool}"]`);
        if (activeBtn) activeBtn.classList.add('active');

        // Atualiza ícone do toggle para refletir ferramenta ativa
        this._updateToggleIcon(tool);

        // Canvas captura eventos apenas com ferramenta de desenho
        this.canvas.style.pointerEvents = isDrawingTool ? 'auto' : 'none';
        // touch-action: none BLOQUEIA scroll — só ativa ao desenhar
        this.canvas.style.touchAction   = isDrawingTool ? 'none' : 'auto';

        // Badge de modo desenho (mobile)
        if (isDrawingTool) {
            this.modeBadge.classList.remove('dt2-hidden');
            this._updateBadgeColor(tool);
        } else {
            this.modeBadge.classList.add('dt2-hidden');
        }

        // Toolbar: indica visualmente a ferramenta ativa no ícone toggle
        this.toolbar.classList.toggle('dt2-drawing-active', isDrawingTool);

        // Ajusta slider
        if (tool === 'highlighter') {
            this.sizeSlider.value = Math.max(this.penSize, 20);
        } else if (tool === 'eraser') {
            this.sizeSlider.value = this.eraserSize;
        } else if (isDrawingTool) {
            this.sizeSlider.value = this.penSize;
        }
        this.sizeLabel.textContent = `${this.sizeSlider.value}px`;

        this._updateCursorPreview();
        this._updateCursor();
    }

    _updateToggleIcon(tool) {
        const icons = {
            cursor:      `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 000-1.41l-2.34-2.34a1 1 0 00-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>`,
            'pen-blue':  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 000-1.41l-2.34-2.34a1 1 0 00-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>`,
            'pen-red':   `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 000-1.41l-2.34-2.34a1 1 0 00-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>`,
            'pen-green': `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 000-1.41l-2.34-2.34a1 1 0 00-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>`,
            highlighter: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M18.5 1.15L17.35 0 10.27 7.08l1.15 1.15L8.35 11.3l-1.15-1.15L6.05 11.3l3.37 3.37 1.15-1.15-1.15-1.15 3.07-3.07 1.15 1.15L18.5 1.15zM5 19h14v2H5z"/></svg>`,
            eraser:      `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M16.24 3.56l4.95 4.94c.78.79.78 2.05 0 2.84L12 20.53a4.008 4.008 0 01-5.66 0L2.81 17c-.78-.79-.78-2.05 0-2.84l10.6-10.6c.79-.78 2.05-.78 2.83 0zM4.22 15.58l3.54 3.53c.78.79 2.04.79 2.83 0l3.53-3.53-6.36-6.36-3.54 3.36z"/></svg>`,
        };
        this.toggleBtn.innerHTML = icons[tool] || icons.cursor;
    }

    _updateBadgeColor(tool) {
        const colors = {
            'pen-blue':   '#60a5fa',
            'pen-red':    '#f87171',
            'pen-green':  '#34d399',
            highlighter:  '#fde047',
            eraser:       '#94a3b8',
        };
        const dot = this.modeBadge.querySelector('.dt2-badge-dot');
        if (dot) dot.style.background = colors[tool] || '#fff';
    }

    _updateCursorPreview() {
        const tool = this.currentTool;
        const size = parseInt(this.sizeSlider.value);
        const preview = this.cursorPreview;

        // Cores explícitas — sem color-mix() para compatibilidade Android
        const colorMap = {
            'pen-blue':   '#60a5fa',
            'pen-red':    '#f87171',
            'pen-green':  '#34d399',
            highlighter:  'rgba(253,224,71,0.65)',
            eraser:       'rgba(255,255,255,0.18)',
        };

        if (tool === 'cursor' || !colorMap[tool]) {
            preview.style.display = 'none';
            return;
        }

        const displaySize = Math.min(Math.max(size, 8), 40);
        Object.assign(preview.style, {
            display:      'block',
            width:        displaySize + 'px',
            height:       displaySize + 'px',
            background:   colorMap[tool],
            borderRadius: tool === 'eraser' ? '4px' : '50%',
            border:       tool === 'eraser' ? '1px solid rgba(255,255,255,0.35)' : 'none',
        });
    }

    _updateCursor() {
        const t = this.currentTool;
        this.canvas.style.cursor =
            t === 'cursor' ? 'default' :
            t === 'eraser' ? 'cell'    : 'crosshair';
    }

    /* ══════════════════ DESENHO ══════════════════ */
    _startDraw(e) {
        if (this.currentTool === 'cursor') return;
        this.isDrawing = true;
        this.lastX = e.clientX;
        this.lastY = e.clientY;
        this._pushUndo();
        // Captura o ponteiro: garante receber pointermove mesmo fora do canvas
        try { this.canvas.setPointerCapture(e.pointerId); } catch(_) {}
    }

    _continueDraw(e) {
        if (!this.isDrawing) return;
        // Evita scroll enquanto desenha em telas touch
        if (e.cancelable) e.preventDefault();

        const x   = e.clientX;
        const y   = e.clientY;
        const ctx = this.ctx;
        const sz  = parseInt(this.sizeSlider.value);

        ctx.beginPath();
        ctx.moveTo(this.lastX, this.lastY);
        ctx.lineTo(x, y);
        ctx.lineCap  = 'round';
        ctx.lineJoin = 'round';

        switch (this.currentTool) {
            case 'eraser':
                ctx.globalCompositeOperation = 'destination-out';
                ctx.strokeStyle = 'rgba(0,0,0,1)';
                ctx.lineWidth   = sz;
                break;
            case 'highlighter':
                ctx.globalCompositeOperation = 'source-over';
                ctx.strokeStyle = 'rgba(253,224,71,0.32)';
                ctx.lineWidth   = sz;
                break;
            case 'pen-blue':
                ctx.globalCompositeOperation = 'source-over';
                ctx.strokeStyle = '#60a5fa';
                ctx.lineWidth   = sz;
                break;
            case 'pen-red':
                ctx.globalCompositeOperation = 'source-over';
                ctx.strokeStyle = '#f87171';
                ctx.lineWidth   = sz;
                break;
            case 'pen-green':
                ctx.globalCompositeOperation = 'source-over';
                ctx.strokeStyle = '#34d399';
                ctx.lineWidth   = sz;
                break;
            default:
                ctx.strokeStyle = '#ffffff';
                ctx.lineWidth   = sz;
        }

        ctx.stroke();
        this.lastX = x;
        this.lastY = y;
    }

    _stopDraw(e) {
        if (!this.isDrawing) return;
        this.isDrawing = false;
        this.ctx.globalCompositeOperation = 'source-over';
        try {
            if (e && e.pointerId !== undefined) {
                this.canvas.releasePointerCapture(e.pointerId);
            }
        } catch(_) {}
    }

    /* ══════════════════ UNDO / CLEAR ══════════════════ */
    _pushUndo() {
        try {
            const snap = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);
            this.undoStack.push(snap);
            if (this.undoStack.length > this.MAX_UNDO) this.undoStack.shift();
        } catch(e) {}
    }

    _undo() {
        if (!this.undoStack.length) return;
        this.ctx.putImageData(this.undoStack.pop(), 0, 0);
    }

    _clearCanvas() {
        this._pushUndo();
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }

    // API pública para app.js
    clearCanvas() { this._clearCanvas(); }

    /* ══════════════════ DRAGGABLE (desktop) ══════════════════ */
    _makeDraggable() {
        let dragging = false, sx, sy, origR, origB;
        const h = this.toolbar;

        h.addEventListener('pointerdown', e => {
            if (e.target.closest('.dt2-btn, .dt2-slider, .dt2-size-wrap, .dt2-toggle-btn')) return;
            dragging = true;
            sx = e.clientX; sy = e.clientY;
            const r = h.getBoundingClientRect();
            origR = window.innerWidth  - r.right;
            origB = window.innerHeight - r.bottom;
            h.style.transition = 'none';
            h.setPointerCapture(e.pointerId);
        });

        h.addEventListener('pointermove', e => {
            if (!dragging) return;
            h.style.right  = (origR + sx - e.clientX) + 'px';
            h.style.bottom = (origB + sy - e.clientY) + 'px';
        });

        const stopDrag = () => { dragging = false; h.style.transition = ''; };
        h.addEventListener('pointerup',     stopDrag);
        h.addEventListener('pointercancel', stopDrag);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.drawingTool = new DrawingTool();
});
