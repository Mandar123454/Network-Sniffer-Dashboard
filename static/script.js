let protocolChart = null;
let sizeChart = null;
let currentPage = 1;
let globalPackets = [];

const protocolSelect = document.getElementById('protocolFilter');
const categorySelect = document.getElementById('categoryFilter');
const searchBox = document.getElementById('searchBox');
const rowsPerPageSelect = document.getElementById('rowsPerPage');
const pageInfo = document.getElementById('pageInfo');
const prevBtn = document.getElementById('prevPage');
const nextBtn = document.getElementById('nextPage');

async function loadData() {
    const proto = protocolSelect.value;
    const cat = categorySelect.value;

    const res = await fetch(`/data?protocol=${proto}&category=${cat}&limit=200`);
    const data = await res.json();

    document.getElementById('total').innerText = data.total;

    // Pretty-print stats
    document.getElementById('proto').innerText = JSON.stringify(data.stats, null, 2);
    document.getElementById('cat').innerText = JSON.stringify(data.cat_stats, null, 2);

    globalPackets = data.packets.slice().reverse(); // newest first

    updateProtocolChart(data.stats);
    updateSizeChart(data.time_labels, data.sizes);
    renderTable();
}

function updateProtocolChart(stats) {
    const ctx = document.getElementById('protocolChart').getContext('2d');
    const labels = Object.keys(stats);
    const values = Object.values(stats);

    if (!protocolChart) {
        protocolChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels,
                datasets: [{
                    label: 'Packets',
                    data: values,
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        ticks: { color: '#e5e7eb' },
                        grid: { color: 'rgba(148, 163, 184, 0.2)' }
                    },
                    y: {
                        ticks: { color: '#e5e7eb' },
                        grid: { color: 'rgba(148, 163, 184, 0.2)' }
                    }
                }
            }
        });
    } else {
        protocolChart.data.labels = labels;
        protocolChart.data.datasets[0].data = values;
        protocolChart.update();
    }
}

function updateSizeChart(timeLabels, sizes) {
    const ctx = document.getElementById('sizeChart').getContext('2d');

    if (!sizeChart) {
        sizeChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: timeLabels,
                datasets: [{
                    label: 'Packet Length',
                    data: sizes,
                    tension: 0.3,
                    borderWidth: 1,
                    pointRadius: 0
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        ticks: { color: '#e5e7eb' },
                        grid: { color: 'rgba(148, 163, 184, 0.2)' }
                    },
                    y: {
                        ticks: { color: '#e5e7eb' },
                        grid: { color: 'rgba(148, 163, 184, 0.2)' }
                    }
                }
            }
        });
    } else {
        sizeChart.data.labels = timeLabels;
        sizeChart.data.datasets[0].data = sizes;
        sizeChart.update();
    }
}

function renderTable() {
    const tbody = document.getElementById('table-body');
    tbody.innerHTML = "";

    const term = (searchBox.value || "").toLowerCase();
    const perPage = parseInt(rowsPerPageSelect.value, 10);

    // Filter by search
    const filtered = globalPackets.filter(pkt => {
        const combined = `${pkt.src || ''} ${pkt.dst || ''} ${pkt.proto} ${pkt.category} ${pkt.info}`.toLowerCase();
        return combined.includes(term);
    });

    const totalPages = Math.max(1, Math.ceil(filtered.length / perPage));
    if (currentPage > totalPages) currentPage = totalPages;

    const start = (currentPage - 1) * perPage;
    const end = start + perPage;
    const pageData = filtered.slice(start, end);

    pageData.forEach(pkt => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${pkt.time}</td>
            <td>${pkt.src || ''}</td>
            <td>${pkt.dst || ''}</td>
            <td>${pkt.proto}</td>
            <td>${pkt.category}</td>
            <td>${pkt.len}</td>
            <td>${pkt.info}</td>
        `;
        tbody.appendChild(tr);
    });

    pageInfo.innerText = `Page ${currentPage} / ${totalPages} (showing ${pageData.length} of ${filtered.length})`;
}

document.getElementById('applyFilters').addEventListener('click', () => {
    currentPage = 1;
    loadData();
});

searchBox.addEventListener('input', () => {
    currentPage = 1;
    renderTable();
});

rowsPerPageSelect.addEventListener('change', () => {
    currentPage = 1;
    renderTable();
});

prevBtn.addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        renderTable();
    }
});

nextBtn.addEventListener('click', () => {
    const perPage = parseInt(rowsPerPageSelect.value, 10);
    const term = (searchBox.value || "").toLowerCase();
    const filtered = globalPackets.filter(pkt => {
        const combined = `${pkt.src || ''} ${pkt.dst || ''} ${pkt.proto} ${pkt.category} ${pkt.info}`.toLowerCase();
        return combined.includes(term);
    });
    const totalPages = Math.max(1, Math.ceil(filtered.length / perPage));
    if (currentPage < totalPages) {
        currentPage++;
        renderTable();
    }
});

// Auto refresh every 2 seconds
setInterval(loadData, 2000);
loadData();
