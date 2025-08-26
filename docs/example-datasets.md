# **Example Space-Based Datasets**

Explore our comprehensive collection of high-resolution space-based satellite datasets categorized by product, use case, and asset type.

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />

<style>
  body {
    background-color: #ffffff;
    font-family: "Inter", sans-serif;
  }

  .container {
    max-width: 100%;
  }

  .filters {
    position: sticky;
    top: 2rem;
  }

  @media (max-width: 768px) {
    .filters {
      position: static;
    }
      #catalog {
    grid-template-columns: 1fr;
    justify-items: center;
  }

  .card-wrapper {
    width: 90%;
    max-width: 340px;
  }

  .card {
    width: 100% !important;
  }
  }

  .filter-card {
    background-color: white;
    border-radius: 16px;
    padding: 0.5rem 0.75rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
    margin-bottom: 1.5rem;
  }

  .filters h4 {
    margin-top: 1.5rem;
    margin-bottom: 0.75rem;
  }

  .d-flex.flex-wrap {
    gap: 0.25rem;
  }

  .filter-button {
    font-size: 0.6rem !important;
    font-weight: 500;
    border-radius: 999px;
    padding: 2px 8px;
    margin: 0.25rem 0.35rem 0.35rem 0;
    border: 2px solid transparent;
    background-color: #f1f3f5;
    color: #333;
    white-space: nowrap;
  }

  .filter-button.active {
    font-weight: 600;
    background-color: #213953ff;
    color: white;
    border-color: #22384fff;
  }

  .filters h5.fw-bold {
  color: #111;
  font-weight: 700;
  }

  .card-wrapper {
    flex: 0 0 auto;
    width: 300px;
    margin-bottom: 1.5rem;
  }

  .card {
    border: none;
    border-radius: 10px;
    overflow: hidden;
    background-color: #ffffffff;
    box-shadow: 0 6px 16px rgba(0, 0, 0, 0.06);
    transition: all 0.25s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
  }
  .card:hover {
    background-color: white !important;
  }

  .card-body {
    padding: 0.75rem 1rem;
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    text-align: left;
    gap: 0.1rem;
  }

  .card-body h6.fw-bold {
    font-size: 0.9rem;
    font-weight: 700;
    color: #212529;
    margin: 0.3rem 0 0.2rem;
  }

  .card-description {
    font-size: 0.65rem;
    line-height: 1.4;
    color: #6c757d;
  }

  .tag {
    font-size: 0.65rem;
    font-weight: 600;
    padding: 0.25em 0.75em;
    border-radius: 999px;
    display: inline-block;
    line-height: 1;
  }

  .tag-product {
    background-color: white;
    color: #0d6efd;
    border: 1px solid #0d6efd;
  }

  .tag-free {
    background-color: #f1f3f5;
    color: #495057;
    border: none;
  }

  .tag-paid {
    background-color: #ef4444;
    color: white;
    border: none;
  }

  .location {
      background-color: #f1f3f5;
      font-size: 0.65rem;
      font-weight: 600;
      padding: 0.3rem 0.75rem;
      border-radius: 999px;
      display: inline-block;
      color: #495057;
      margin: 0.4rem 0 0.8rem;
    }

  .download-button {
    margin-top: 0.1rem; 
    border: 1px solid #dee2e6;
    font-weight: 600;
    padding: 6px 12px;
    border-radius: 12px;
    text-align: center;
    display: inline-block;
    color: #213953ff;
    background-color: #ffffff;
    text-decoration: none;
    font-size: 0.75rem;
    transition: all 0.25s ease;
    box-shadow: none;
  }

  .download-button:hover {
    background-color: #213953ff;
    color: #fff !important;
  }

  .card-image {
      display: block;
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: 1;
      position: relative;
      }

  .carousel-inner {
    aspect-ratio: 16 / 9;
    overflow: hidden;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
  }

  .modal-content {
    border-radius: 10px;
    font-family: 'Inter', sans-serif;
    padding: 1rem;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
  }

  .modal-header .modal-title {
    font-size: 0.8rem;
    font-weight: 700;
    color: #000000ff;
    margin-bottom: 0;
  }

  .modal-body p {
    font-size: 0.8rem;
    color: #6b7280;
    margin-bottom: 0.8rem;
  }

  .form-label {
    font-weight: 600;
    font-size: 0.7rem;
    margin-bottom: 0.15rem;
  }

  .form-control {
    font-size: 0.7rem;
    padding: 0.4rem 0.6rem;
    border-radius: 6px;
    border: 1px solid #d1d5db;
  }

  .form-control:focus {
    border-color: #4f46e5;
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.15);
  }

  .modal-body .mb-3 {
    margin-bottom: 0.7rem !important;
  }

  .modal-footer {
    border-top: none;
    padding-top: 0;
    margin-top: 0.5rem;
    gap: 0.5rem;
  }

  .btn-secondary {
    background-color: #f3f4f6;
    color: #213953ff;
    border: none;
    font-weight: 500;
    padding: 0.4rem 0.9rem;
    font-size: 0.75rem;
    border-radius: 6px;
  }

  .btn-primary {
    background-color: #213953ff;
    color: white;
    border: none;
    font-weight: 600;
    font-size: 0.75rem;
    padding: 0.4rem 1rem;
    border-radius: 6px;
  }

  .btn-primary:hover {
    background-color: #213953ff;
  }

  #thankYouModal .modal-dialog {
    max-width: 400px;
  }

  #thankYouModal .modal-content {
    border-radius: 16px;
    padding: 2rem 1.5rem;
    border: none;
    box-shadow: 0 8px 40px rgba(0, 0, 0, 0.2);
    background-color: white;
    position: relative;
    text-align: center;
  }

  #thankYouModal .btn-close {
    position: absolute;
    top: 1rem;
    right: 1rem;
    font-size: 0.85rem;
    opacity: 0.6;
  }

  #thankYouModal .btn-close:hover {
    opacity: 1;
  }

  #thankYouModal .thank-you-title {
    font-size: 0.85rem;
    font-weight: 700;
    color: #1a1a1a;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
  }

  #thankYouModal .thank-you-msg {
    font-size: 0.75rem;
    color: #6c757d;
    margin-bottom: 1.25rem;
    line-height: 1.4;
    text-align: center;
  }

  #thankYouSpinner {
    display: block;
    margin: 0 auto;
    width: 1rem;
    height: 1rem;
    color: #213953ff;
    border-color: #e0e0e0;
    border-top-color: #213953ff;
  }


  #catalog {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
    gap: 1.5rem;
    align-items: stretch;
  }

  .card-wrapper {
    max-width: 100%;
  }
</style>

<div class="container pt-2">
  <div class="row">
    <div class="col-md-4 filters">
  <div class="filter-card">
    <h5 class="fw-bold">Product</h5>
    <div id="filter-product" class="d-flex flex-wrap"></div>
  </div>
  <div class="filter-card">
    <h5 class="fw-bold">Use Cases</h5>
    <div id="filter-usecase" class="d-flex flex-wrap"></div>
  </div>
  <div class="filter-card">
    <h5 class="fw-bold">Price</h5>
    <div id="filter-price" class="d-flex flex-wrap"></div>
  </div>
</div>
    <div class="col-md-8">
      <div class="row justify-content-center" id="catalog"></div>
    </div>
  </div>
</div>
<div class="modal fade" id="downloadModal" tabindex="-1" aria-labelledby="downloadModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="downloadModalLabel">Download Dataset</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>

      <div class="modal-body">
        <p>You're about to download: <strong id="datasetTitle"></strong></p>
        <form id="downloadForm">
          <div class="mb-3">
            <label for="name" class="form-label">Name</label>
            <input type="text" class="form-control" id="name" placeholder="Your full name" />
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" class="form-control" id="email" placeholder="your.email@company.com" />
          </div>
          <div class="mb-3">
            <label for="company" class="form-label">Company</label>
            <input type="text" class="form-control" id="company" placeholder="Your company name" />
          </div>
        </form>
      </div>

      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
        <button type="submit" form="downloadForm" class="btn btn-primary">DOWNLOAD DATASET →</button>
      </div>
    </div>
  </div>
</div>

<!-- Thank You Modal -->
<div class="modal fade" id="thankYouModal" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-sm">
    <div class="modal-content text-center p-4">
      <button type="button" class="btn-close ms-auto" data-bs-dismiss="modal" aria-label="Close"></button>
      <h5 class="thank-you-title fw-bold mt-3">Thank You!</h5>
      <p class="thank-you-msg text-muted mb-3"></p>
      <div class="spinner-border text-primary" id="thankYouSpinner" role="status" style="display: none;"></div>
    </div>
  </div>
</div>

<script>
  let datasets = [], filtered = [], filters = { product: [], use_case: [], price: [] };

  function createTag(label, type, value) {
    return `<button class="btn btn-outline-secondary btn-sm filter-button" data-type="${type}" data-value="${value}">${label}</button>`;
  }

  function renderFilters() {
    const productCounts = {};
    const useCaseCounts = {};
    const priceCounts = {};

    datasets.forEach(d => {
      productCounts[d.product] = (productCounts[d.product] || 0) + 1;
      priceCounts[d.price] = (priceCounts[d.price] || 0) + 1;
      d.use_cases.forEach(u => {
        useCaseCounts[u] = (useCaseCounts[u] || 0) + 1;
      });
    });

    const productHTML = Object.keys(productCounts)
      .map(p => createTag(`${p} (${productCounts[p]})`, "product", p)).join("");
    document.getElementById("filter-product").innerHTML = productHTML;

    const usecaseHTML = Object.keys(useCaseCounts)
      .map(u => createTag(`${u} (${useCaseCounts[u]})`, "use_case", u)).join("");
    document.getElementById("filter-usecase").innerHTML = usecaseHTML;

    const priceHTML = Object.keys(priceCounts)
      .map(p => createTag(`${p} (${priceCounts[p]})`, "price", p)).join("");
    document.getElementById("filter-price").innerHTML = priceHTML;

    document.querySelectorAll(".filter-button").forEach(btn => {
      btn.addEventListener("click", () => {
        const type = btn.dataset.type;
        const val = btn.dataset.value;
        const list = filters[type];

        if (list.includes(val)) {
          filters[type] = list.filter(v => v !== val);
          btn.classList.remove("active");
        } else {
          filters[type].push(val);
          btn.classList.add("active");
        }

        renderCatalog();
      });
    });
  }


  function renderCatalog() {
    filtered = datasets.filter(d => {
      const matchProduct = !filters.product.length || filters.product.includes(d.product);
      const matchPrice = !filters.price.length || filters.price.includes(d.price);
      const matchUseCase = !filters.use_case.length || d.use_cases.some(u => filters.use_case.includes(u));
      return matchProduct && matchPrice && matchUseCase;
    });

    const container = document.getElementById("catalog");
    container.innerHTML = "";

    filtered.forEach((d, i) => {
  const carouselId = `carousel-${i}`;
  const indicators = d.images.map((_, j) =>
    `<button type="button" data-bs-target="#${carouselId}" data-bs-slide-to="${j}" class="${j === 0 ? 'active' : ''}" aria-label="Slide ${j + 1}"></button>`
  ).join('');

  const slides = d.images.map((img, j) =>
    `<div class="carousel-item ${j === 0 ? 'active' : ''}">
      <img src="${img}" class="d-block w-100 card-image" alt="Slide ${j + 1}">
    </div>`
  ).join('');

  const card = document.createElement("div");
  card.className = "card-wrapper";

  card.innerHTML = `
    <div class="card w-100">
      <div id="${carouselId}" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          ${indicators}
        </div>
        <div class="carousel-inner">
          ${slides}
        </div>
        ${d.images.length > 1 ? `
          <button class="carousel-control-prev" type="button" data-bs-target="#${carouselId}" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#${carouselId}" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>` : ''
        }
      </div>
      
      <div class="card-body d-flex flex-column">
        <div class="mb-2">
          <span class="tag tag-product">${d.product}</span>
          <span class="tag ${d.price.toLowerCase() === 'free' ? 'tag-free' : 'tag-paid'}">${d.price.toUpperCase()}</span>
        </div>
        <h6 class="fw-bold">${d.title}</h6>
        <div class="location">📍 ${d.locations.join(', ')}</div>
        <p class="text-muted small">${d.description}</p>
        <a class="download-button mt-auto" onclick='openModal(${JSON.stringify(d)})'>DOWNLOAD DATASET →</a>
      </div>
    </div>
  `;

  container.appendChild(card);
});
  }


  fetch("/constellr/product-lst/datasets.json")
    .then(res => res.json())
    .then(data => {
      datasets = data;
      renderFilters();
      renderCatalog();
    });

let currentDataset = null;

function openModal(dataset) {
  currentDataset = dataset;
  document.getElementById("datasetTitle").innerText = dataset.title;

  const modalEl = document.getElementById("downloadModal");
  const modal = new bootstrap.Modal(modalEl);
  modal.show();
}


function showThankYouModal(datasetTitle, isFree) {
  const modalEl = document.getElementById("thankYouModal");
  const modalTitle = modalEl.querySelector(".thank-you-title");
  const modalMsg = modalEl.querySelector(".thank-you-msg");
  const spinner = modalEl.querySelector(".spinner-border");

  modalTitle.textContent = "Thank You!";
  spinner.style.display = "inline-block"; // show spinner

  if (isFree) {
    modalMsg.innerHTML = `Your dataset is downloading now.<br><strong>${datasetTitle}</strong>`;
  } else {
    modalMsg.innerHTML = `Redirecting you to the dataset purchase page.<br><strong>${datasetTitle}</strong>`;
  }

  const thankYouModal = new bootstrap.Modal(modalEl);
  thankYouModal.show();

  setTimeout(() => {
    spinner.style.display = "none";
    thankYouModal.hide();

    if (isFree) {
      window.open(currentDataset.download_url, "_blank");
    } else {
      window.open("https://www.constellr.com/", "_blank");
    }
  }, 2500);
}

document.getElementById("downloadForm").addEventListener("submit", async function (e) {
  e.preventDefault();
  console.log("Submitted!")
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const company = document.getElementById("company").value.trim();

  if (name || email || company) {
    await fetch("/api/send-download-info", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name,
        email,
        company,
        dataset: currentDataset.title,
      }),
    });
  }

   const formModalEl = document.getElementById("downloadModal");
   if (formModalEl) {
        const existingModal = bootstrap.Modal.getInstance(formModalEl);
   if (existingModal) {
        existingModal.hide();
    }
    }

  showThankYouModal(
    currentDataset.title,
    currentDataset.price.toLowerCase() === "free"
  );
});
</script>