<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Popcat Game</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #ffffff;
            flex-direction: column;
        }
        img {
            width: 200px;
            height: 200px;
        }
        h1 {
            font-size: 24px;
        }
    </style>
</head>
<body>
    <h1>Pop Count: <span id="popCount">0</span></h1>
    <img id="popcat" src="assets/closed_mouth_image.png" alt="Popcat">

    <script>
        let popCount = 0;
        const popcatImage = document.getElementById('popcat');
        const popCountDisplay = document.getElementById('popCount');

        popcatImage.addEventListener('mousedown', () => {
            popcatImage.src = 'open_mouth.png';
            popCount++;
            popCountDisplay.textContent = popCount;
        });

        popcatImage.addEventListener('mouseup', () => {
            popcatImage.src = 'closed_mouth.png';
        });
    </script>
</body>
</html>
