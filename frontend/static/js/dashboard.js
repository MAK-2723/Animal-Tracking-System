const token = localStorage.getItem('token');
const dataDisplay = document.getElementById('dataDisplay');
const alertList = document.getElementById('alertList');

if (!token) {
    window.location.href = '/login';
}

fetch('/api/dashboard_data', {
    headers: { 'Authorization': `Bearer ${token}` }
})
.then(res => res.json())
.then(data => {
    if (data.error) {
        dataDisplay.textContent = 'Error loading data.';
    } else {
        dataDisplay.style.display = 'none';

        const categoryCounts = {};
        const locationCounts = {};

        data.forEach(item => {
            const category = item.category || 'Unknown';
            const location = item.location || 'Unknown';

            categoryCounts[category] = (categoryCounts[category] || 0) + 1;
            locationCounts[location] = (locationCounts[location] || 0) + 1;
    });

    const categoryLabels = Object.keys(categoryCounts);
    const categoryData = Object.values(categoryCounts);

    const locationLabels = Object.keys(locationCounts);
    const locationData = Object.values(locationCounts);

    new Chart(document.getElementById('categoryChart'), {
        type: 'bar',
        data: {
            labels: categoryLabels,
            datasets: [{
                label: 'Animal Category Counts',
                data: categoryData,
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    new Chart(document.getElementById('locationChart'), {
        type: 'pie',
        data: {
            labels: locationLabels,
            datasets: [{
                label: 'Animal Detections by Location',
                data: locationData,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)',
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(153, 102, 255, 0.6)'
              ]
            }]
        },
        options: {
            responsive: true
        }
    });
    }
})
.catch(err => {
    dataDisplay.textContent = 'An error occurred while loading the dashboard.';
    console.error(err);
});

fetch('/api/alerts', {
    headers: { 'Authorization': `Bearer ${token}` }
})
.then(res => res.json())
.then(alerts => {
    alertList.innerHTML = '';
    if (alerts.length === 0) {
        alertList.innerHTML = '<li>No alerts found.</li>';
        return;
    }
    alerts.forEach(alert => {
        const item = document.createElement('li');
        item.textContent = `${alert.animal} (${alert.category}) at ${alert.location} on ${new Date(alert.timestamp).toLocaleString()}`;
        alertList.appendChild(item);
    });
})
.catch(err => {
    alertList.textContent = 'Error loading alerts.';
    console.error(err);
});

function logout() {
    localStorage.removeItem('token');
    window.location.href = '/login';
}