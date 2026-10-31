// Mobile menu
const toggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".site-nav");

if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
  });
  nav.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      nav.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    })
  );
}

// Gallery lightbox
const box = document.querySelector(".lightbox");

if (box) {
  const img = box.querySelector("img");
  const close = () => {
    box.classList.remove("open");
    box.setAttribute("aria-hidden", "true");
    img.removeAttribute("src");
  };

  document.querySelectorAll(".gallery a").forEach((a) =>
    a.addEventListener("click", (e) => {
      e.preventDefault();
      img.src = a.href;
      box.classList.add("open");
      box.setAttribute("aria-hidden", "false");
    })
  );
  box.addEventListener("click", (e) => {
    if (e.target !== img) close();
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") close();
  });
}

document.querySelectorAll("[data-year]").forEach((el) => {
  el.textContent = new Date().getFullYear();
});
