class DrawingTool {
    constructor() {
        this.initDOM();
        this.initCanvas();
        this.bindEvents();
        this.currentTool = 'cursor'; // 'cursor', 'pen-blue', 'pen-red', 'highlighter', 'eraser'
        this.isDrawing = false;
        this.lastX = 0;
        this.lastY = 0;
    }

    initDOM() {
        this.canvas = document.createElement('canvas');
        this.canvas.id = 'drawing-canvas';
        document.body.appendChild(this.canvas);
        this.ctx = this.canvas.getContext('2d', { willReadFrequently: true });
        
        this.canvas.style.position = 'absolute';
        this.canvas.style.top = '0';
        this.canvas.style.left = '0';
        this.canvas.style.pointerEvents = 'none';
        this.canvas.style.zIndex = '999';
        
        // This makes the highlighter effect perfect over the DOM text without darkening itself
        this.canvas.style.mixBlendMode = 'multiply'; 
    }

    initCanvas() {
        this.resizeCanvas();
        const resizeObserver = new ResizeObserver(() => {
            this.resizeCanvas(true);
        });
        resizeObserver.observe(document.body);
    }

    resizeCanvas(restore = false) {
        let imageData;
        if (restore && this.canvas.width > 0 && this.canvas.height > 0) {
            try { imageData = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height); } catch(e) {}
        }
        
        const scrollHeight = Math.max(
            document.body.scrollHeight, document.documentElement.scrollHeight
        );
        const scrollWidth = Math.max(
            document.body.scrollWidth, document.documentElement.scrollWidth
        );
        
        this.canvas.width = scrollWidth;
        this.canvas.height = scrollHeight;
        
        if (restore && imageData) {
            this.ctx.putImageData(imageData, 0, 0);
        }
    }

    bindEvents() {
        // Modern Pointer Events for zero lag and universal touch/mouse support
        this.canvas.addEventListener('pointerdown', this.startDrawing.bind(this));
        this.canvas.addEventListener('pointermove', this.draw.bind(this));
        this.canvas.addEventListener('pointerup', this.stopDrawing.bind(this));
        this.canvas.addEventListener('pointerout', this.stopDrawing.bind(this));
        this.canvas.addEventListener('pointercancel', this.stopDrawing.bind(this));

        // Toolbar Events mapped to pointerdown for instant response
        document.querySelectorAll('.dt-btn').forEach(btn => {
            btn.addEventListener('pointerdown', (e) => {
                e.preventDefault(); // Prevent double-firing or focus issues on mobile
                const tool = btn.dataset.tool;
                
                if (tool === 'clear') {
                    this.clearCanvas();
                    return;
                }
                
                this.setTool(tool);
                document.querySelectorAll('.dt-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
            });
        });
    }
    
    setTool(tool) {
        this.currentTool = tool;
        if (tool === 'cursor') {
            this.canvas.style.pointerEvents = 'none';
        } else {
            this.canvas.style.pointerEvents = 'auto';
        }
    }

    startDrawing(e) {
        if (this.currentTool === 'cursor') return;
        this.isDrawing = true;
        // e.pageX/pageY automatically accounts for scrolling on an absolute canvas
        this.lastX = e.pageX;
        this.lastY = e.pageY;
    }

    draw(e) {
        if (!this.isDrawing) return;
        e.preventDefault(); // Prevent scrolling while drawing on touch devices
        
        const currentX = e.pageX;
        const currentY = e.pageY;
        
        this.ctx.beginPath();
        this.ctx.moveTo(this.lastX, this.lastY);
        this.ctx.lineTo(currentX, currentY);
        
        this.ctx.lineCap = 'round';
        this.ctx.lineJoin = 'round';
        
        // Reset to normal drawing mode before setting specific tool
        this.ctx.globalCompositeOperation = 'source-over';
        
        if (this.currentTool === 'pen-blue') {
            this.ctx.strokeStyle = '#2563eb';
            this.ctx.lineWidth = 3;
        } else if (this.currentTool === 'pen-red') {
            this.ctx.strokeStyle = '#ef4444';
            this.ctx.lineWidth = 3;
        } else if (this.currentTool === 'highlighter') {
            this.ctx.strokeStyle = '#fde047'; // Solid yellow (blend mode handles transparency)
            this.ctx.lineWidth = 20;
        } else if (this.currentTool === 'eraser') {
            this.ctx.globalCompositeOperation = 'destination-out';
            this.ctx.strokeStyle = 'rgba(0,0,0,1)';
            this.ctx.lineWidth = 30;
        }
        
        this.ctx.stroke();
        
        this.lastX = currentX;
        this.lastY = currentY;
    }

    stopDrawing() {
        this.isDrawing = false;
    }

    clearCanvas() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.drawingTool = new DrawingTool();
});
