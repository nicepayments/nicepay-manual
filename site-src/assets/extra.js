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

const openFoldForHash = () => {
  let id;
  try {
    id = decodeURIComponent(location.hash.slice(1));
  } catch (error) {
    return;
  }
  const target = id && document.getElementById(id);
  if (!target) return;
  let fold = target.closest("details.spec-fold");
  if (!fold) return;
  const inSummary = target.closest("summary") === fold.querySelector(":scope > summary");
  while (fold) {
    fold.open = true;
    fold = fold.parentElement.closest("details.spec-fold");
  }
  if (!inSummary) target.scrollIntoView();
};

window.addEventListener("hashchange", openFoldForHash);
openFoldForHash();
