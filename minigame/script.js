// ゲームの初期設定
let score = 0;
let gameInterval = null;
let timerInterval = null;  // タイマー用の変数
let timeLeft = 30;  // 制限時間（秒）

// UFOの要素を取得
const ufo = document.querySelector(".ufo");
const scoreElement = document.getElementById("score");
const startButton = document.getElementById("start-button");
const timerElement = document.createElement("p");  // タイマー表示用の要素を作成

// タイマー表示を画面に追加
document.body.insertBefore(timerElement, startButton);

// UFOをランダムに表示する関数
function randomizeUFO() {
    // UFOを非表示にする
    ufo.style.display = "none";

    // 1秒ごとにUFOをランダムに表示
    setTimeout(() => {
        const randomTop = Math.floor(Math.random() * (window.innerHeight - 150));  // UFOの位置をランダム設定
        const randomLeft = Math.floor(Math.random() * (window.innerWidth - 120));  // UFOの位置をランダム設定

        // UFOをランダムな位置に表示
        ufo.style.top = `${randomTop}px`;
        ufo.style.left = `${randomLeft}px`;
        ufo.style.display = "block";
    }, Math.random() * 2000);  // 0〜2秒後に表示
}

// クリックでスコアを加算する処理
ufo.addEventListener("click", () => {
    score++;
    scoreElement.textContent = score;
    ufo.style.display = "none";  // UFOを隠す
});

// 制限時間をカウントダウンする関数
function startTimer() {
    timerInterval = setInterval(() => {
        timeLeft--;
        timerElement.textContent = `残り時間: ${timeLeft}秒`;

        if (timeLeft <= 0) {
            endGame();  // 時間が終了したらゲーム終了
        }
    }, 1000);
}

// ゲーム開始関数
function startGame() {
    score = 0;
    timeLeft = 30;  // 制限時間をリセット
    scoreElement.textContent = score;
    timerElement.textContent = `残り時間: ${timeLeft}秒`;
    startButton.disabled = true;

    // UFOをランダムに表示
    gameInterval = setInterval(randomizeUFO, 1000);

    // タイマーを開始
    startTimer();
}

// ゲーム終了関数
function endGame() {
    clearInterval(gameInterval);  // UFO表示のインターバルを停止
    clearInterval(timerInterval);  // タイマーを停止
    alert("ゲーム終了！最終スコア: " + score);
    startButton.disabled = false;  // ゲーム終了後、ボタンを再度有効にする
}

// ゲームスタートボタンのクリックイベント
startButton.addEventListener("click", startGame);
