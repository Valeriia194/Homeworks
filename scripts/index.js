// Burger menu
function openNav() {
  document.getElementById("mobileNav").style.display = "block";
}
function closeNav() {
  document.getElementById("mobileNav").style.display = "none";
}

// Form Registration
const getDataFromField = (element) => {
    const VALUE = element.value;
    const TYPE = element.getAttribute("name")

    if (TYPE == "last_name") {
        if (VALUE.length >= 3) {
            return VALUE
        } else {
            alert("Lastname to short")
            return null
        }
    }
    return VALUE
}


//start

document.addEventListener("DOMContentLoaded", () => {
    const USER_DATA = JSON.parse(localStorage.getItem("user"));
    console.log(USER_DATA);

    const CHECK_BOX = document.querySelector(".form__input_checkbox");
    const SUBMIT_BTN = document.querySelector(".form__input_sumbit");
    const REGISTER_FORM = document.querySelector(".form");
    const INPUT_LAST_NAME = document.querySelector(".form__input_second_name");
    const INPUT_NAME = document.querySelector(".form__input_first_name");
    const INPUT_EMAIL = document.querySelector(".form__input_email");
    const INPUT_PASSWORD = document.querySelector(".form__input_password");


    if(USER_DATA){
        const {userName, userLastName, userEmail, userPassword} = USER_DATA;
        INPUT_NAME.value = userName;
        INPUT_LAST_NAME.value = userLastName;
        INPUT_EMAIL.value = userEmail;
        INPUT_PASSWORD.value = userPassword;
    }

    CHECK_BOX.addEventListener("click", function (e) {
        const CHECK_BOX_VALUE = CHECK_BOX.checked;
        CHECK_BOX_VALUE ? SUBMIT_BTN.disabled = false : SUBMIT_BTN.disabled = true;
    })

    REGISTER_FORM.addEventListener("submit", (e)=>{
        e.preventDefault();
        // get data form
        let role = getUserRole(LF_BLOCK);
        let userLastName = getDataFromField(INPUT_LAST_NAME);
        let userName = getDataFromField(INPUT_NAME);
        let userEmail = getDataFromField(INPUT_EMAIL);
        let userPassword = getDataFromField(INPUT_PASSWORD);

        const USER_DATA = {
            role, userName, userLastName, userEmail, userPassword
        }

        localStorage.setItem("user", JSON.stringify(USER_DATA));
        
        sessionStorage.setItem("user", JSON.stringify(USER_DATA));


        console.log("USER_DATA", USER_DATA)
    })
})