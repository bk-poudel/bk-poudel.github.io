document.addEventListener('DOMContentLoaded', function () {
    if (document.querySelector('.floating-icons-container')) {
        return;
    }

    const layer = document.createElement('div');
    layer.className = 'floating-icons-container';

    const icons = [
        'android-icon-svgrepo-com.svg',
        'arduino-svgrepo-com.svg',
        'arduinodroid-svgrepo-com.svg',
        'artificial-intelligence-svgrepo-com.svg',
        'c-sharp-16-svgrepo-com.svg',
        'car-svgrepo-com.svg',
        'circuit-board-microchip-svgrepo-com.svg',
        'code-svgrepo-com.svg',
        'drone-svgrepo-com.svg',
        'drone-tech-svgrepo-com.svg',
        'hardware-chip-outline-svgrepo-com.svg',
        'hardware-svgrepo-com.svg',
        'humanoid-robot-svgrepo-com.svg',
        'humanoid-svgrepo-com.svg',
        'industrial-robot-factory-svgrepo-com.svg',
        'industrial-robot-svgrepo-com.svg',
        'kaggle-svgrepo-com.svg',
        'machine-learning-02-svgrepo-com.svg',
        'machine-learning-model-svgrepo-com.svg',
        'mechanical-arm-robotics-svgrepo-com.svg',
        'nvidia-logo-svgrepo-com.svg',
        'opencv-svgrepo-com.svg',
        'python-svgrepo-com.svg',
        'pytorch-svgrepo-com.svg',
        'raspberrypi-svgrepo-com.svg',
        'robot-arm-1-svgrepo-com.svg',
        'robot-artificial-intelligence-svgrepo-com.svg',
        'robot-svgrepo-com (1).svg',
        'robot-svgrepo-com.svg',
        'solidworks-svgrepo-com.svg',
        'sparkfun-svgrepo-com.svg',
        'tensorflow-svgrepo-com.svg',
        'vision-svgrepo-com.svg',
        'vscode-16-svgrepo-com.svg'
    ];

    const iconData = [];
    icons.forEach(function (iconName) {
        const icon = document.createElement('img');
        icon.src = '../icons/' + iconName;
        icon.className = 'floating-icon';
        icon.alt = iconName.replace('-svgrepo-com.svg', '').replace(/-/g, ' ');

        const size = 60 + Math.random() * 30;
        icon.style.width = size + 'px';
        icon.style.height = size + 'px';

        const x = Math.random() * Math.max(window.innerWidth - size, 1);
        const y = Math.random() * Math.max(window.innerHeight - size, 1);
        const speed = 0.5 + Math.random() * 1.5;
        const angle = Math.random() * Math.PI * 2;
        const vx = Math.cos(angle) * speed;
        const vy = Math.sin(angle) * speed;
        const rotationSpeed = (Math.random() - 0.5) * 2;

        layer.appendChild(icon);
        iconData.push({
            element: icon,
            x: x,
            y: y,
            vx: vx,
            vy: vy,
            size: size,
            rotation: 0,
            rotationSpeed: rotationSpeed
        });
    });

    document.body.appendChild(layer);

    function animate() {
        const width = window.innerWidth;
        const height = window.innerHeight;

        iconData.forEach(function (data) {
            data.x += data.vx;
            data.y += data.vy;

            if (data.x <= 0 || data.x >= width - data.size) {
                data.vx *= -1;
                data.x = Math.max(0, Math.min(data.x, width - data.size));
            }

            if (data.y <= 0 || data.y >= height - data.size) {
                data.vy *= -1;
                data.y = Math.max(0, Math.min(data.y, height - data.size));
            }

            data.rotation += data.rotationSpeed;
            data.element.style.transform = 'translate(' + data.x + 'px, ' + data.y + 'px) rotate(' + data.rotation + 'deg)';
        });

        window.requestAnimationFrame(animate);
    }

    animate();
});