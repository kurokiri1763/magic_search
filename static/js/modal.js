document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('search-modal'); // モーダル本体
    const openButton = document.getElementById('open-modal'); // モーダルを開くボタン
    const closeButton = document.getElementById('close-modal'); // モーダルを閉じるボタン

    // モーダルを開く
    openButton.addEventListener('click', function () {
        modal.style.display = 'block';
    });

    // モーダルを閉じる
    closeButton.addEventListener('click', function () {
        modal.style.display = 'none';
    });

    // モーダル外をクリックしたときに閉じる
    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});
