const submitBtnHome = document.getElementById("submitBtnHome");
const homeShortnerForm = document.getElementById('homeShortnerForm');
const aliasDashboard = document.getElementById('aliasDashboard');
if (submitBtnHome != null) {

    submitBtnHome.addEventListener('click', () => {
        homeShortnerForm.submit();
        homeShortnerForm.reset();
    })
}

function copyText(id) {
    let inputTag = document.getElementById(`shorted-${id}`);
    let btn = document.getElementById(`copyBtn_${id}`);

    inputTag.select();
    document.execCommand("copy")
    console.log("copied")
    var tooltip = new bootstrap.Tooltip(btn, {
        animation: true,
        delay: { "show": 800, "hide": 100 },
        placement: 'top',
        title: 'copied'
    });
    tooltip.show()
    //tooltip.hide()

}
/*==============================================*/

if (aliasDashboard != null) {
    aliasDashboard.addEventListener('keyup', () => {
        //let reg = /[a-z]/gi;
        aliasDashboard.value = aliasDashboard.value.replace(new RegExp(".(?=.{0," + (aliasDashboard.value.length - 5) + "}$)", "g"), '')
        //aliasDashboard.value = aliasDashboard.value.replace(reg, "");
        console.log(aliasDashboard.value)
        console.log("reloaded")
    })
}