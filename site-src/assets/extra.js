document.addEventListener("click", async (event) => {
  const button = event.target.closest("[data-copy-md]");
  if (!button) return;
  const label = button.textContent;
  try {
    const response = await fetch(button.dataset.copyMd);
    await navigator.clipboard.writeText(await response.text());
    button.textContent = "복사됨";
  } catch (error) {
    button.textContent = "복사 실패";
  }
  setTimeout(() => { button.textContent = label; }, 1500);
});
