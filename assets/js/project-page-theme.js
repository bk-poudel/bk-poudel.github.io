document.addEventListener('DOMContentLoaded', function () {
    if (document.querySelector('.floating-icons-container')) {
        return;
    }

    const layer = document.createElement('div');
    layer.className = 'floating-icons-container';

    const icons = [
        'android.svg',
        'arduino.svg',
        'arduinodroid.svg',
        'artificial-intelligence.svg',
        'c-sharp.svg',
        'car.svg',
        'circuit-board.svg',
        'code.svg',
        'drone-tech.svg',
        'drone.svg',
        'hardware-chip.svg',
        'hardware.svg',
        'humanoid-robot.svg',
        'humanoid.svg',
        'industrial-robot-factory.svg',
        'industrial-robot.svg',
        'kaggle.svg',
        'machine-learning-model.svg',
        'machine-learning.svg',
        'mechanical-arm.svg',
        'nvidia.svg',
        'opencv.svg',
        'python.svg',
        'pytorch.svg',
        'raspberrypi.svg',
        'robot-ai.svg',
        'robot-alt.svg',
        'robot-arm.svg',
        'robot.svg',
        'solidworks.svg',
        'sparkfun.svg',
        'tensorflow.svg',
        'vision.svg',
        'vscode.svg'
    ];

    const iconData = [];
    icons.forEach(function (iconName) {
        const icon = document.createElement('img');
        icon.src = '../assets/icons/' + iconName;
        icon.className = 'floating-icon';
        icon.alt = iconName.replace('.svg', '').replace(/-/g, ' ');

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