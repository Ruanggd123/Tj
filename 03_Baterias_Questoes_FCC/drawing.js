/**
 * DrawingTool — v2.0
 * Reescrito do zero para corrigir:
 *  - Coordenadas erradas ao rolar a página (fixed canvas overlay)
 *  - Marca-texto funcional em fundo escuro (canvas sobreposto com opacity)
 *  - Cursor personalizado para cada ferramenta
 *  - Tamanho ajustável da caneta via slider
 *  - Desfazer (Ctrl+Z / botão)
 *  - Toolbar integrada ao tema dark do site
 */
class DrawingTool {
    constructor() {
        this.currentTool = 'cursor';
        this.isDrawing   = false;
        this.lastX       = 0;
        this.lastY       = 0;

        // Undo stack (imageData snapshots)
        this.undoStack = [];
        this.MAX_UNDO  = 20;

        this.penSize = 3;
        this.eraserSize = 28;

        this._createCanvas();
        this._createToolbar();
        this._bindEvents();
    }

    /* ───────────────── Canvas ───────────────── */
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
            zIndex:        '998',
            opacity:       '1',
        });

        document.body.appendChild(this.canvas);
        this._resizeCanvas();

        // Redimensiona ao mudar viewport
        window.addEventListener('resize', () => this._resizeCanvas(true));
    }

    _resizeCanvas(restore = false) {
        let snapshot;
        if (restore && this.canvas.width > 0) {
            try { snapshot = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height); } catch(e) {}
        }
        this.canvas.width  = window.innerWidth;
        this.canvas.height = window.innerHeight;
        if (restore && snapshot) {
            this.ctx.putImageData(snapshot, 0, 0);
        }
    }

    /* ───────────────── Toolbar ───────────────── */
    _createToolbar() {
        // Remove toolbar antiga do HTML se existir (já está em todas_questoes_fcc.html)
        const old = document.querySelector('.drawing-toolbar');
        if (old) old.remove();

        this.toolbar = document.createElement('div');
        this.toolbar.className = 'dt2-toolbar';
        this.toolbar.innerHTML = `
            <!-- Cursor -->
            <button class="dt2-btn active" data-tool="cursor" title="Cursor (Modo Normal — Ctrl+0)">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M4 0l16 12.279-6.951 1.17 4.325 8.817-3.62 1.734-4.287-8.898-5.467 4.898z"/></svg>
            </button>

            <div class="dt2-divider"></div>

            <!-- Caneta Azul -->
            <button class="dt2-btn" data-tool="pen-blue" title="Caneta Azul (Ctrl+1)" style="--tool-color:#60a5fa">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 000-1.41l-2.34-2.34a1 1 0 00-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
            </button>

            <!-- Caneta Vermelha -->
            <button class="dt2-btn" data-tool="pen-red" title="Caneta Vermelha (Ctrl+2)" style="--tool-color:#f87171">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 000-1.41l-2.34-2.34a1 1 0 00-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
            </button>

            <!-- Caneta Verde -->
            <button class="dt2-btn" data-tool="pen-green" title="Caneta Verde (Ctrl+3)" style="--tool-color:#34d399">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 000-1.41l-2.34-2.34a1 1 0 00-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
            </button>

            <div class="dt2-divider"></div>

            <!-- Marca-texto -->
            <button class="dt2-btn" data-tool="highlighter" title="Marca-texto Amarelo (Ctrl+4)" style="--tool-color:#fde047">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M18.5 1.15L17.35 0 10.27 7.08l1.15 1.15L8.35 11.3l-1.15-1.15L6.05 11.3l3.37 3.37 1.15-1.15-1.15-1.15 3.07-3.07 1.15 1.15L18.5 1.15zM5 19h14v2H5z"/></svg>
            </button>

            <div class="dt2-divider"></div>

            <!-- Borracha -->
            <button class="dt2-btn" data-tool="eraser" title="Borracha (Ctrl+5)">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M16.24 3.56l4.95 4.94c.78.79.78 2.05 0 2.84L12 20.53a4.008 4.008 0 01-5.66 0L2.81 17c-.78-.79-.78-2.05 0-2.84l10.6-10.6c.79-.78 2.05-.78 2.83 0zM4.22 15.58l3.54 3.53c.78.79 2.04.79 2.83 0l3.53-3.53-6.36-6.36-3.54 3.36z"/></svg>
            </button>

            <div class="dt2-divider"></div>

            <!-- Slider de tamanho -->
            <div class="dt2-size-wrap" title="Tamanho do traço">
                <span class="dt2-size-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="14" height="14"><circle cx="12" cy="12" r="5"/></svg>
                </span>
                <input type="range" class="dt2-slider" id="dt2-slider" min="1" max="40" value="3">
                <span class="dt2-size-label" id="dt2-size-label">3px</span>
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
        `;

        document.body.appendChild(this.toolbar);
        this.sizeSlider  = this.toolbar.querySelector('#dt2-slider');
        this.sizeLabel   = this.toolbar.querySelector('#dt2-size-label');
        this.cursorPreview = this.toolbar.querySelector('#dt2-cursor-preview');
    }

    /* ───────────────── Eventos ───────────────── */
    _bindEvents() {
        // Botões da toolbar
        this.toolbar.querySelectorAll('.dt2-btn[data-tool]').forEach(btn => {
            btn.addEventListener('pointerdown', e => {
                e.preventDefault();
                const tool = btn.dataset.tool;
                if (tool === 'clear') { this._clearCanvas(); return; }
                if (tool === 'undo')  { this._undo(); return; }
                this._setTool(tool);
            });
        });

        // Slider de tamanho
        this.sizeSlider.addEventListener('input', () => {
            const v = parseInt(this.sizeSlider.value);
            this.penSize = v;
            this.sizeLabel.textContent = `${v}px`;
            this._updateCursorPreview();
        });

        // Atalhos de teclado
        document.addEventListener('keydown', e => {
            if (e.ctrlKey || e.metaKey) {
                if (e.key === 'z' || e.key === 'Z') { e.preventDefault(); this._undo(); return; }
                const map = { '0': 'cursor', '1': 'pen-blue', '2': 'pen-red', '3': 'pen-green', '4': 'highlighter', '5': 'eraser' };
                if (map[e.key]) { e.preventDefault(); this._setTool(map[e.key]); }
            }
            if (e.key === 'Escape') this._setTool('cursor');
        });

        // Desenho — usa clientX/Y (coordenadas do viewport, correto para canvas fixed)
        this.canvas.addEventListener('pointerdown', e => this._startDraw(e));
        this.canvas.addEventListener('pointermove', e => this._continueDraw(e));
        this.canvas.addEventListener('pointerup',   () => this._stopDraw());
        this.canvas.addEventListener('pointerout',  () => this._stopDraw());
        this.canvas.addEventListener('pointercancel', () => this._stopDraw());

        // Drag da toolbar
        this._makeDraggable();
    }

    /* ───────────────── Ferramentas ───────────────── */
    _setTool(tool) {
        this.currentTool = tool;

        // Atualiza botão ativo
        this.toolbar.querySelectorAll('.dt2-btn[data-tool]').forEach(b => b.classList.remove('active'));
        const active = this.toolbar.querySelector(`.dt2-btn[data-tool="${tool}"]`);
        if (active) active.classList.add('active');

        // Canvas recebe eventos apenas quando ferramenta ativa
        this.canvas.style.pointerEvents = (tool === 'cursor') ? 'none' : 'auto';

        // Ajusta slider ao tamanho da ferramenta atual
        if (tool === 'highlighter') {
            this.sizeSlider.value = Math.max(this.penSize, 20);
            this.sizeLabel.textContent = `${this.sizeSlider.value}px`;
        } else if (tool === 'eraser') {
            this.sizeSlider.value = this.eraserSize;
            this.sizeLabel.textContent = `${this.eraserSize}px`;
        } else if (tool !== 'cursor') {
            this.sizeSlider.value = this.penSize;
            this.sizeLabel.textContent = `${this.penSize}px`;
        }

        this._updateCursorPreview();
        this._updateCursor();
    }

    _updateCursorPreview() {
        const tool = this.currentTool;
        const size = parseInt(this.sizeSlider.value);
        const preview = this.cursorPreview;

        const colorMap = {
            'pen-blue':   '#60a5fa',
            'pen-red':    '#f87171',
            'pen-green':  '#34d399',
            'highlighter':'rgba(253, 224, 71, 0.6)',
            'eraser':     'rgba(255,255,255,0.2)',
        };

        if (tool === 'cursor' || !colorMap[tool]) {
            preview.style.display = 'none';
            return;
        }

        const displaySize = Math.min(Math.max(size, 8), 40);
        preview.style.display = 'block';
        preview.style.width   = displaySize + 'px';
        preview.style.height  = displaySize + 'px';
        preview.style.background = colorMap[tool];
        preview.style.borderRadius = tool === 'eraser' ? '4px' : '50%';
        preview.style.border = tool === 'eraser' ? '1px solid rgba(255,255,255,0.4)' : 'none';
    }

    _updateCursor() {
        const t = this.currentTool;
        if (t === 'cursor' || t === 'undo' || t === 'clear') {
            this.canvas.style.cursor = 'default';
        } else if (t === 'eraser') {
            this.canvas.style.cursor = 'cell';
        } else {
            this.canvas.style.cursor = 'crosshair';
        }
    }

    /* ───────────────── Desenho ───────────────── */
    _startDraw(e) {
        if (this.currentTool === 'cursor') return;
        this.isDrawing = true;
        this.lastX = e.clientX;
        this.lastY = e.clientY;
        // Snapshot para undo
        this._pushUndo();
    }

    _continueDraw(e) {
        if (!this.isDrawing) return;
        e.preventDefault();

        const x = e.clientX;
        const y = e.clientY;
        const ctx = this.ctx;
        const size = parseInt(this.sizeSlider.value);

        ctx.beginPath();
        ctx.moveTo(this.lastX, this.lastY);
        ctx.lineTo(x, y);
        ctx.lineCap  = 'round';
        ctx.lineJoin = 'round';

        if (this.currentTool === 'eraser') {
            ctx.globalCompositeOperation = 'destination-out';
            ctx.strokeStyle = 'rgba(0,0,0,1)';
            ctx.lineWidth = size;
        } else if (this.currentTool === 'highlighter') {
            ctx.globalCompositeOperation = 'source-over';
            ctx.strokeStyle = `rgba(253, 224, 71, 0.35)`;
            ctx.lineWidth = size;
        } else {
            ctx.globalCompositeOperation = 'source-over';
            const colorMap = {
                'pen-blue':  '#60a5fa',
                'pen-red':   '#f87171',
                'pen-green': '#34d399',
            };
            ctx.strokeStyle = colorMap[this.currentTool] || '#ffffff';
            ctx.lineWidth = size;
        }

        ctx.stroke();
        this.lastX = x;
        this.lastY = y;
    }

    _stopDraw() {
        this.isDrawing = false;
        // Restaura composite após uso do eraser
        this.ctx.globalCompositeOperation = 'source-over';
    }

    /* ───────────────── Undo ───────────────── */
    _pushUndo() {
        try {
            const snap = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);
            this.undoStack.push(snap);
            if (this.undoStack.length > this.MAX_UNDO) {
                this.undoStack.shift();
            }
        } catch(e) {}
    }

    _undo() {
        if (this.undoStack.length === 0) return;
        const snap = this.undoStack.pop();
        this.ctx.putImageData(snap, 0, 0);
    }

    /* ───────────────── Limpar ───────────────── */
    _clearCanvas() {
        this._pushUndo();
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }

    // Exposto para app.js (limpa ao trocar de página)
    clearCanvas() {
        this._clearCanvas();
    }

    /* ───────────────── Arrastar toolbar ───────────────── */
    _makeDraggable() {
        let dragging = false, startX, startY, origRight, origBottom;

        const handle = this.toolbar;

        handle.addEventListener('pointerdown', e => {
            // Só arrasta se clicar no fundo da toolbar (não nos botões)
            if (e.target.closest('.dt2-btn') || e.target.closest('.dt2-slider') || e.target.closest('.dt2-size-wrap')) return;
            dragging = true;
            startX = e.clientX;
            startY = e.clientY;
            const rect = handle.getBoundingClientRect();
            origRight  = window.innerWidth  - rect.right;
            origBottom = window.innerHeight - rect.bottom;
            handle.style.transition = 'none';
            handle.setPointerCapture(e.pointerId);
        });

        handle.addEventListener('pointermove', e => {
            if (!dragging) return;
            const dx = startX - e.clientX;
            const dy = startY - e.clientY;
            handle.style.right  = (origRight  + dx) + 'px';
            handle.style.bottom = (origBottom + dy) + 'px';
        });

        handle.addEventListener('pointerup',    () => { dragging = false; handle.style.transition = ''; });
        handle.addEventListener('pointercancel',() => { dragging = false; handle.style.transition = ''; });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.drawingTool = new DrawingTool();
    // Seleciona cursor por padrão
    window.drawingTool._setTool('cursor');
});
