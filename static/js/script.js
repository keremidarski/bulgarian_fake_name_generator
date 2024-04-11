// Function to update puppet information on the webpage
function updatePuppetInfo(data) {
    console.log('Updating puppet info:', data);

    // Update photo
    const photoFrame = document.getElementById('photoFrame');
    photoFrame.style.backgroundImage = `url(${data.photo})`;

    // Update puppet info
    const puppetInfo = {
        'cyrillicFirstName': data.cyrillic_first_name,
        'cyrillicFamilyName': data.cyrillic_family_name,
        'gender': data.gender,
        'dob': data.dob,
        'age': data.age + ' години',
        'starSign': data.star_sign,
        'egn': data.egn,
        'address': data.address,
        'phoneNumber': data.phone_number,
        'creditCard': data.credit_card,
        'email': data.email,
        'username': data.username,
        'password': data.password,
        'websiteDomain': data.website_domain
    };

    for (const [key, value] of Object.entries(puppetInfo)) {
        const element = document.getElementById(key);
        if (element) {
            element.textContent = value;
        } else {
            console.error(`Element with ID '${key}' not found.`);
        }
    }
}

// Function to generate a random puppet
async function generateRandomPuppet() {
    console.log('Generating random puppet...');

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                gender: 'random'
            })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        updatePuppetInfo(data);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

// Automatically generate a random puppet when the page is loaded
generateRandomPuppet();
