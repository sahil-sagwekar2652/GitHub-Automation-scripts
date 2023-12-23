const cont = document.getElementById('contributor');
const repoUrl = 'https://api.github.com/repos/sahil-sagwekar2652/GitHub-Automation-scripts/contributors';

async function fetchContributors(pageNumber) {
    const perPage = 100;
    const url = `${repoUrl}?page=${pageNumber}&per_page=${perPage}`;

    const response = await fetch(url);

    if (!response.ok) {
        throw new Error(`Failed to fetch contributors data. Status code: ${response.status}`);
    }

    return response.json();
}

function createContributorCard(contributor) {
    const contributorCard = document.createElement('div');
    contributorCard.classList.add('contributor-card');

    const avatarImg = document.createElement('img');
    avatarImg.src = contributor.avatar_url;
    avatarImg.alt = `${contributor.login}'s Picture`;

    const loginLink = document.createElement('a');
    loginLink.href = contributor.html_url;
    loginLink.appendChild(avatarImg);

    contributorCard.appendChild(loginLink);

    return contributorCard;
}

async function fetchAllContributors() {
    let allContributors = [];
    let pageNumber = 1;

    try {
        while (true) {
            const contributorsData = await fetchContributors(pageNumber);

            if (contributorsData.length === 0) {
                break;
            }

            allContributors = allContributors.concat(contributorsData);
            pageNumber++;
        }

        // Display contributors in the honeycomb-like layout
        allContributors.forEach((contributor) => {
            const contributorCard = createContributorCard(contributor);
            cont.appendChild(contributorCard);
        });
    } catch (error) {
        console.error(error);
    }
}

fetchAllContributors();
