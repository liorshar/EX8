
function getUser(){
    let id = document.getElementById("user_id2").value;
    fetch('https://reqres.in/api/users/'+id).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data) {
    const curr_main = document.querySelector("div");
    curr_main.innerHTML = `
    <img src="${response_obj_data.avatar}" alt="Picture"/>
    <div>
        <span>First name:${response_obj_data.first_name} </span><br>
        <span>Last name:${response_obj_data.last_name} </span><br>
        <span>ID: ${response_obj_data.id}</span><br>
        <span>Email: ${response_obj_data.email}</span><br>
    </div>
    `;

}