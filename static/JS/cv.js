function validationEmail(mailInput,messageArea){
    const inpObj = document.getElementById(mailInput);
    if (!inpObj.checkValidity()) {
    document.getElementById(messageArea).innerHTML = inpObj.validationMessage;
    }   
}

function validationComment(commentInput,messageArea){
    const inpObj = document.getElementById(commentInput);
    if (!inpObj.checkValidity()) {
    document.getElementById(messageArea).innerHTML = inpObj.validationMessage;
    }   
}