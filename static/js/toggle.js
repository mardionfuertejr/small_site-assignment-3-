function toggleText() {
    const previewText = document.getElementById("preview-text");
    const fullText = document.getElementById("full-text");
    const btn = document.getElementById("toggle-btn");

    if (fullText.style.display === "none") {
        // Show full text
        previewText.style.display = "none";
        fullText.style.display = "inline";
        btn.textContent = "Show less";
    } else {
        // Show preview text
        previewText.style.display = "inline";
        fullText.style.display = "none";
        btn.textContent = "Read more";
    }
}
