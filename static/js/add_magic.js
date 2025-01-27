document.addEventListener('DOMContentLoaded', function () {
    const magicTypeSelect = document.getElementById('id_magic_type'); // 魔法の系統フィールド
    const extendedEffects = document.getElementById('extended-effects'); // 拡張効果フィールド
    const spellField = document.getElementById('spell-field'); // 詠唱フィールド

    // 拡張効果フィールドの表示/非表示を制御
    function toggleExtendedEffects() {
        if (magicTypeSelect.value === 'abyssgazer') {
            extendedEffects.style.display = 'block'; // 「奈落魔法」の場合に表示
        } else {
            extendedEffects.style.display = 'none'; // その他の場合は非表示
        }
    }

    // 詠唱フィールドの表示/非表示を制御
    function toggleSpellField() {
        const allowedTypes = ['sorcerer', 'conjurer', 'wizard']; // 詠唱を表示する魔法の系統
        if (allowedTypes.includes(magicTypeSelect.value)) {
            spellField.style.display = 'block'; // 指定された系統なら表示
        } else {
            spellField.style.display = 'none'; // その他の場合は非表示
        }
    }

    // 初期状態を設定
    toggleExtendedEffects();
    toggleSpellField();

    // 魔法の系統が変更されたときのイベント
    magicTypeSelect.addEventListener('change', function () {
        toggleExtendedEffects();
        toggleSpellField();
    });
});
