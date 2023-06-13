var profile = document.getElementById('profile_form')
var submitButton = document.getElementById('submit')
var initialNickname = document.getElementById('nickname').value
console.log(initialNickname);

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