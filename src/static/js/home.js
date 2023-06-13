var profile = document.getElementById('profile_form')
var submitButton = document.getElementById('submit')

async function setNickname() {
    const response = await fetch('http://127.0.0.1:5000/nickname', { method: 'GET' })
    const responseJson = await response.json();
    nicknameInput.value = responseJson.nickname
}

setNickname()
var nicknameInput = document.getElementById('nickname');
var initialNickname = nicknameInput.value

function showSubmitButton() {
    submitButton.style.visibility = 'visible'
}

function hideSubmitButton() {
    submitButton.style.visibility = 'hidden'
}

profile.addEventListener('input', () => {
    if (initialNickname != document.getElementById('nickname').value) {
        showSubmitButton()
    } else {
        hideSubmitButton()
    }
})