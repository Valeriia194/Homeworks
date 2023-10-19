



document.addEventListener("DOMContentLoaded", () => {
    const SUBMIT_BTN = document.querySelector(".form__input_sumbit");
    const REGISTER_FORM = document.querySelector(".form");
    const INPUT_LAST_NAME = document.querySelector(".form__input_second_name");


    REGISTER_FORM.addEventListener("submit", (e)=>{
        e.preventDefault();
        // get data form
        let role = getUserRole(LF_BLOCK);
        let lastUserName = getLastNameUser(INPUT_LAST_NAME);

        const USER_DATA = {
            role, lastUserName
        }
        console.log("USER_DATA", USER_DATA)
    })
})