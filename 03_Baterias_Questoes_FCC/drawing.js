/**
 * DrawingTool v3.0 — Definitivo para Android/iOS/Desktop
 *
 * Bugs corrigidos vs v2.1:
 *  - touch-action: none aplicado via CSS class (não JS inline) — browser respeita ANTES do toque
 *  - Rastreio de pointerId — sem saltos em multi-touch
 *  - Listeners de move/up no document filtrados por pointerId (não no window inteiro)
 *  - Canvas não apaga ao girar o celular (usa off-screen canvas de backup)
 *  - Toolbar mobile usa display:none real (não max-width) — mais compatível
 *  - Badge reposicionado dinamicamente acima da toolbar
 *  - Botões com touch feedback (active state via CSS class)
 *  - RAF (requestAnimationFrame) para desenho suave
 *  - visibilitychange: encerra traçado se app vai para background
 */
class DrawingTool {
    constructor() {
        this.tool        = 'cursor';
        this.isDrawing   = false;
        this.activePtr   = null;   // pointerId ativo
        this.lastX       = 0;
        this.lastY       = 0;
        this.undoStack   = [];
        this.MAX_UNDO    = 20;
        this.penSize     = 4;
        this.eraserSize  = 30;
        this.rafPending  = false;
        this.pendingX    = 0;
        this.pendingY    = 0;

        // Off-screen canvas para preservar desenho em resize/rotação
        this.backupCanvas = document.createElement('canvas');
        this.backupCtx    = this.backupCanvas.getContext('2d');

        this._isMobile = () => window.innerWidth <= 768;

        this._initCanvas();
        this._initToolbar();
        this._bindEvents();
    }

    /* ══════════════════════════════════════════════
       CANVAS
    ══════════════════════════════════════════════ */
    _initCanvas() {
        this.canvas = document.createElement('canvas');
        this.canvas.id = 'dt3-canvas';
        // CSS class controla touch-action (não JS inline)
        // .dt3-drawing-mode { touch-action: none; pointer-events: auto; }
        this.canvas.className = 'dt3-canvas-base';
        this.ctx = this.canvas.getContext('2d');
        document.body.appendChild(this.canvas);
        this._resizeCanvas();

        // Debounce resize — evita múltiplas chamadas seguidas (teclado virtual Android)
        let resizeTimer;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(() => this._resizeCanvas(true), 120);
        });

        // Encerra traçado se app vai para background (Android home button)
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) this._stopDraw();
        });
    }

    _resizeCanvas(restore = false) {
        // Salva desenho atual no off-screen canvas
        if (restore && this.canvas.width > 0 && this.canvas.height > 0) {
            this.backupCanvas.width  = this.canvas.width;
            this.backupCanvas.height = this.canvas.height;
            this.backupCtx.clearRect(0, 0, this.backupCanvas.width, this.backupCanvas.height);
            this.backupCtx.drawImage(this.canvas, 0, 0);
        }

        this.canvas.width  = window.innerWidth;
        this.canvas.height = window.innerHeight;

        // Restaura do off-screen canvas
        if (restore && this.backupCanvas.width > 0) {
            this.ctx.drawImage(this.backupCanvas, 0, 0);
        }
    }

    /* ══════════════════════════════════════════════
       TOOLBAR
    ══════════════════════════════════════════════ */
    _initToolbar() {
        // Remove possíveis toolbars antigas
        document.querySelectorAll('.dt2-toolbar, .drawing-toolbar, #dt3-toolbar').forEach(el => el.remove());

        this.toolbar = document.createElement('div');
        this.toolbar.id = 'dt3-toolbar';
        this.toolbar.className = 'dt3-tb';

        this.toolbar.innerHTML = `
            <!-- FAB toggle: sempre visível -->
            <button class="dt3-fab" id="dt3-fab" aria-label="Ferramentas de anotação">
                <span class="dt3-fab-icon" id="dt3-fab-icon">
                    ${this._penSVG(20)}
                </span>
                <span class="dt3-fab-ring" id="dt3-fab-ring"></span>
            </button>

            <!-- Painel de ferramentas -->
            <div class="dt3-panel" id="dt3-panel" role="toolbar" aria-label="Ferramentas de desenho">
                <button class="dt3-btn dt3-cursor active" data-tool="cursor" aria-label="Cursor / Scroll">
                    ${this._cursorSVG()}
                </button>

                <div class="dt3-sep"></div>

                <button class="dt3-btn dt3-blue" data-tool="pen-blue" aria-label="Caneta Azul">
                    ${this._penSVG()}
                </button>
                <button class="dt3-btn dt3-red" data-tool="pen-red" aria-label="Caneta Vermelha">
                    ${this._penSVG()}
                </button>
                <button class="dt3-btn dt3-green" data-tool="pen-green" aria-label="Caneta Verde">
                    ${this._penSVG()}
                </button>

                <div class="dt3-sep"></div>

                <button class="dt3-btn dt3-yellow" data-tool="highlighter" aria-label="Marca-texto">
                    ${this._highlightSVG()}
                </button>

                <div class="dt3-sep"></div>

                <button class="dt3-btn dt3-eraser" data-tool="eraser" aria-label="Borracha">
                    ${this._eraserSVG()}
                </button>

                <div class="dt3-sep"></div>

                <!-- Slider tamanho -->
                <div class="dt3-size-wrap">
                    <svg width="12" height="12" viewBox="0 0 12 12" fill="currentColor"><circle cx="6" cy="6" r="4"/></svg>
                    <input class="dt3-slider" id="dt3-slider" type="range" min="1" max="40" value="4" aria-label="Tamanho">
                    <span class="dt3-size-lbl" id="dt3-size-lbl">4px</span>
                </div>

                <div class="dt3-sep"></div>

                <button class="dt3-btn dt3-undo" data-tool="undo" aria-label="Desfazer">
                    ${this._undoSVG()}
                </button>
                <button class="dt3-btn dt3-clear" data-tool="clear" aria-label="Limpar tudo">
                    ${this._clearSVG()}
                </button>
            </div>
        `;

        document.body.appendChild(this.toolbar);

        this.fab      = this.toolbar.querySelector('#dt3-fab');
        this.fabIcon  = this.toolbar.querySelector('#dt3-fab-icon');
        this.fabRing  = this.toolbar.querySelector('#dt3-fab-ring');
        this.panel    = this.toolbar.querySelector('#dt3-panel');
        this.slider   = this.toolbar.querySelector('#dt3-slider');
        this.sizeLbl  = this.toolbar.querySelector('#dt3-size-lbl');

        // Em desktop começa aberto; mobile começa fechado
        if (!this._isMobile()) {
            this.panel.classList.add('dt3-open');
        }
    }

    /* SVG helpers */
    _penSVG(s=18){ return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="${s}" height="${s}"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 000-1.41l-2.34-2.34a1 1 0 00-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>`; }
    _cursorSVG(){ return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M4 0l16 12.279-6.951 1.17 4.325 8.817-3.62 1.734-4.287-8.898-5.467 4.898z"/></svg>`; }
    _highlightSVG(){ return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M18.5 1.15L17.35 0 10.27 7.08l1.15 1.15L8.35 11.3l-1.15-1.15L6.05 11.3l3.37 3.37 1.15-1.15-1.15-1.15 3.07-3.07 1.15 1.15L18.5 1.15zM5 19h14v2H5z"/></svg>`; }
    _eraserSVG(){ return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M16.24 3.56l4.95 4.94c.78.79.78 2.05 0 2.84L12 20.53a4.008 4.008 0 01-5.66 0L2.81 17c-.78-.79-.78-2.05 0-2.84l10.6-10.6c.79-.78 2.05-.78 2.83 0zM4.22 15.58l3.54 3.53c.78.79 2.04.79 2.83 0l3.53-3.53-6.36-6.36-3.54 3.36z"/></svg>`; }
    _undoSVG(){ return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M12.5 8c-2.65 0-5.05.99-6.9 2.6L2 7v9h9l-3.62-3.62c1.39-1.16 3.16-1.88 5.12-1.88 3.54 0 6.55 2.31 7.6 5.5l2.37-.78C21.08 11.03 17.15 8 12.5 8z"/></svg>`; }
    _clearSVG(){ return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M19 4h-3.5l-1-1h-5l-1 1H5v2h14V4zm-3 16H8a2 2 0 01-2-2l-1-11h14L18 18a2 2 0 01-2 2z"/></svg>`; }

    /* ══════════════════════════════════════════════
       EVENTOS
    ══════════════════════════════════════════════ */
    _bindEvents() {
        /* ─── FAB toggle ─── */
        this.fab.addEventListener('pointerdown', e => {
            e.preventDefault();
            e.stopPropagation();
            this._togglePanel();
        });

        /* ─── Botões ─── */
        this.panel.querySelectorAll('.dt3-btn[data-tool]').forEach(btn => {
            btn.addEventListener('pointerdown', e => {
                e.preventDefault();
                e.stopPropagation();
                const t = btn.dataset.tool;
                if (t === 'clear') { this._clearCanvas(); return; }
                if (t === 'undo')  { this._undo(); return; }
                this._setTool(t);
                // Mobile: fecha o painel após selecionar ferramenta de desenho
                if (this._isMobile() && t !== 'cursor') {
                    setTimeout(() => this._closePanel(), 200);
                }
            });
        });

        /* ─── Slider ─── */
        this.slider.addEventListener('input', () => {
            const v = +this.slider.value;
            this.penSize = v;
            this.sizeLbl.textContent = v + 'px';
        });

        /* ─── Fechar painel ao clicar fora ─── */
        document.addEventListener('pointerdown', e => {
            if (this.panel.classList.contains('dt3-open') &&
                !this.toolbar.contains(e.target)) {
                this._closePanel();
            }
        }, { passive: true });

        /* ─── Atalhos teclado ─── */
        document.addEventListener('keydown', e => {
            const mod = e.ctrlKey || e.metaKey;
            if (mod && (e.key === 'z' || e.key === 'Z')) { e.preventDefault(); this._undo(); return; }
            if (mod) {
                const map = { '0':'cursor','1':'pen-blue','2':'pen-red','3':'pen-green','4':'highlighter','5':'eraser' };
                if (map[e.key]) { e.preventDefault(); this._setTool(map[e.key]); }
            }
            if (e.key === 'Escape') this._setTool('cursor');
        });

        /* ─── DESENHO ─────────────────────────────────────────────────
         * pointerdown no canvas inicia o traço e captura o ponteiro.
         * pointermove / pointerup escutam no DOCUMENT mas só processam
         * o pointerId que iniciou o traço — ignora outros dedos/ponteiros.
         */
        this.canvas.addEventListener('pointerdown', e => {
            if (this.tool === 'cursor') return;
            if (this.isDrawing) return;           // já tem um traço ativo
            e.preventDefault();
            this.isDrawing  = true;
            this.activePtr  = e.pointerId;
            this.lastX      = e.clientX;
            this.lastY      = e.clientY;
            this._pushUndo();
            try { this.canvas.setPointerCapture(e.pointerId); } catch(_) {}
        });

        document.addEventListener('pointermove', e => {
            if (!this.isDrawing || e.pointerId !== this.activePtr) return;
            if (e.cancelable) e.preventDefault();
            // RAF: suaviza o traçado no mobile
            this.pendingX = e.clientX;
            this.pendingY = e.clientY;
            if (!this.rafPending) {
                this.rafPending = true;
                requestAnimationFrame(() => {
                    this._drawSegment(this.pendingX, this.pendingY);
                    this.rafPending = false;
                });
            }
        }, { passive: false });

        document.addEventListener('pointerup', e => {
            if (e.pointerId !== this.activePtr) return;
            this._stopDraw();
        });

        document.addEventListener('pointercancel', e => {
            if (e.pointerId !== this.activePtr) return;
            this._stopDraw();
        });

        /* ─── Arrastar toolbar (desktop) ─── */
        this._makeDraggable();
    }

    /* ══════════════════════════════════════════════
       PAINEL
    ══════════════════════════════════════════════ */
    _togglePanel() {
        if (this.panel.classList.contains('dt3-open')) {
            this._closePanel();
        } else {
            this._openPanel();
        }
    }

    _openPanel() {
        this.panel.classList.add('dt3-open');
        this.fab.classList.add('dt3-fab-open');
    }

    _closePanel() {
        this.panel.classList.remove('dt3-open');
        this.fab.classList.remove('dt3-fab-open');
    }

    /* ══════════════════════════════════════════════
       FERRAMENTAS
    ══════════════════════════════════════════════ */
    _setTool(t) {
        this.tool = t;
        const isDrawing = t !== 'cursor';

        // Atualiza botão ativo
        this.panel.querySelectorAll('.dt3-btn[data-tool]').forEach(b => b.classList.remove('active'));
        const btn = this.panel.querySelector(`.dt3-btn[data-tool="${t}"]`);
        if (btn) btn.classList.add('active');

        // Canvas: class CSS controla touch-action e pointer-events juntos
        // .dt3-drawing-mode { touch-action: none; pointer-events: auto; }
        this.canvas.classList.toggle('dt3-drawing-mode', isDrawing);

        // FAB: mostra a cor da ferramenta ativa no anel
        const ringColors = {
            'pen-blue':    '#60a5fa',
            'pen-red':     '#f87171',
            'pen-green':   '#34d399',
            'highlighter': '#fde047',
            'eraser':      '#94a3b8',
            'cursor':      'transparent',
        };
        this.fabRing.style.borderColor = ringColors[t] || 'transparent';
        this.fabRing.style.opacity     = isDrawing ? '1' : '0';

        // FAB: ícone muda para a ferramenta ativa
        this.fabIcon.innerHTML = isDrawing ? this._toolIcon(t) : this._penSVG(20);

        // Ajusta slider
        if (t === 'highlighter') {
            this.slider.value = Math.max(this.penSize, 18);
        } else if (t === 'eraser') {
            this.slider.value = this.eraserSize;
        } else if (isDrawing) {
            this.slider.value = this.penSize;
        }
        this.sizeLbl.textContent = this.slider.value + 'px';

        // Barra de status (badge mobile)
        this._updateStatusBar(t);
    }

    _toolIcon(t) {
        if (t === 'highlighter') return this._highlightSVG();
        if (t === 'eraser')      return this._eraserSVG();
        if (t === 'cursor')      return this._cursorSVG();
        return this._penSVG(20);
    }

    _updateStatusBar(t) {
        // Remove barra existente
        const existing = document.getElementById('dt3-status');
        if (existing) existing.remove();

        if (t === 'cursor') return;

        const labels = {
            'pen-blue':    '✏️ Caneta Azul',
            'pen-red':     '✏️ Caneta Vermelha',
            'pen-green':   '✏️ Caneta Verde',
            'highlighter': '🖊️ Marca-texto',
            'eraser':      '🧹 Borracha',
        };

        const bar = document.createElement('div');
        bar.id = 'dt3-status';
        bar.className = 'dt3-status';
        bar.innerHTML = `
            <span class="dt3-status-dot" data-tool="${t}"></span>
            <span>${labels[t] || t} — Toque para desenhar</span>
            <button class="dt3-status-close" aria-label="Sair do modo desenho">✕ Sair</button>
        `;
        document.body.appendChild(bar);

        bar.querySelector('.dt3-status-close').addEventListener('click', () => {
            this._setTool('cursor');
        });

        // Anima entrada
        requestAnimationFrame(() => bar.classList.add('dt3-status-in'));
    }

    /* ══════════════════════════════════════════════
       DESENHO
    ══════════════════════════════════════════════ */
    _drawSegment(x, y) {
        const ctx = this.ctx;
        const sz  = +this.slider.value;

        ctx.beginPath();
        ctx.moveTo(this.lastX, this.lastY);
        ctx.lineTo(x, y);
        ctx.lineCap  = 'round';
        ctx.lineJoin = 'round';

        switch(this.tool) {
            case 'eraser':
                ctx.globalCompositeOperation = 'destination-out';
                ctx.strokeStyle = 'rgba(0,0,0,1)';
                ctx.lineWidth   = sz;
                break;
            case 'highlighter':
                ctx.globalCompositeOperation = 'source-over';
                ctx.strokeStyle = 'rgba(253,224,71,0.30)';
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

    _stopDraw() {
        if (!this.isDrawing) return;
        this.isDrawing  = false;
        this.activePtr  = null;
        this.rafPending = false;
        this.ctx.globalCompositeOperation = 'source-over';
        try { this.canvas.releasePointerCapture(this.activePtr); } catch(_) {}
    }

    /* ══════════════════════════════════════════════
       UNDO / CLEAR
    ══════════════════════════════════════════════ */
    _pushUndo() {
        try {
            const snap = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);
            this.undoStack.push(snap);
            if (this.undoStack.length > this.MAX_UNDO) this.undoStack.shift();
        } catch(_) {}
    }

    _undo() {
        if (!this.undoStack.length) return;
        this.ctx.putImageData(this.undoStack.pop(), 0, 0);
    }

    _clearCanvas() {
        this._pushUndo();
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }

    // API para app.js
    clearCanvas() { this._clearCanvas(); }

    /* ══════════════════════════════════════════════
       ARRASTAR TOOLBAR (desktop)
    ══════════════════════════════════════════════ */
    _makeDraggable() {
        let drag = false, sx, sy, origR, origB;
        const h = this.toolbar;

        h.addEventListener('pointerdown', e => {
            if (this._isMobile()) return;
            if (e.target.closest('.dt3-btn, .dt3-slider, .dt3-size-wrap, .dt3-fab, .dt3-panel')) return;
            drag = true;
            sx = e.clientX; sy = e.clientY;
            const r = h.getBoundingClientRect();
            origR = window.innerWidth  - r.right;
            origB = window.innerHeight - r.bottom;
            h.style.transition = 'none';
            h.setPointerCapture(e.pointerId);
        });

        h.addEventListener('pointermove', e => {
            if (!drag) return;
            h.style.right  = (origR + sx - e.clientX) + 'px';
            h.style.bottom = (origB + sy - e.clientY) + 'px';
        });

        const endDrag = () => { drag = false; h.style.transition = ''; };
        h.addEventListener('pointerup',     endDrag);
        h.addEventListener('pointercancel', endDrag);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.drawingTool = new DrawingTool();
});
