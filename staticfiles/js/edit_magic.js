document.addEventListener("DOMContentLoaded", function () {
    // 要素を取得
    const magicTypeSelect = document.getElementById("id_magic_type");
    const extendedEffects = document.getElementById("extended-effects");
    const spellField = document.getElementById("spell-field");

    // 詠唱が必要な系統
    const spellRequiredTypes = ["sorcerer", "conjurer", "wizard"];

    // 拡張効果が必要な系統
    const extendedEffectTypes = ["abyssgazer"];

    function updateFields() {
        const selectedType = magicTypeSelect.value;

        // 詠唱が必要かどうか
        spellField.style.display = spellRequiredTypes.includes(selectedType) ? "block" : "none";

        // 拡張効果が必要かどうか
        extendedEffects.style.display = extendedEffectTypes.includes(selectedType) ? "block" : "none";
    }

    // 初期状態を設定
    updateFields();

    // 魔法の系統が変更されたらフィールドを更新
    magicTypeSelect.addEventListener("change", updateFields);
});
