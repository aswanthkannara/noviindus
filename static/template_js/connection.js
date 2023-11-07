function emptyField(act) {
    debugger;
    var Act = document.getElementById(act);
    var myID = Act.id;
    var valid = false;
    if (Act.value != "") {
        valid = true;
    }
    if (valid == false) {
        $('#errorDiv').removeClass("error_class");
        $('#' + myID + '').addClass("required");
        $('#errorDiv').show();
        setTimeout(function () { $('#errorDiv').hide(); }, 3000);
        return false;
    }
}

document.getElementById('CourseForm').addEventListener('submit', function (event) {
    event.preventDefault();
    var data = new FormData();
    var fileInput = document.getElementById('image');
    data.append('image', fileInput.files[0]);
    var name = document.getElementById('title').value;
    var Subtitle = document.getElementById('Subtitle').value;
    if (name.trim() === '') {
        alert('Name is required');
        return;
    }
    if (Subtitle.trim() === '') {
        alert('Subtitle is required');
        return;
    }
    if ($('#image').val() == '') {
        alert('Please upload image');
        return;
    }
    if ($('#amt').val() == '') {
        alert('Please add amount');
        return;
    }
    if ($('#amt2').val() == '') {
        alert('Please add amount in words !');
        return;
    }
    otherData = {
        'name': name,
        'subtitle': Subtitle,
        'amt': $('#amt').val(),
        'amt2': $('#amt2').val(),
        // 'description':$("#description").val()
        'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
    }
    for (var key in otherData) {
        data.append(key, otherData[key]);
    }
    $.ajax({
        url: '/add-new-course/',
        type: "POST",
        contentType: false,
        processData: false,
        data: data,
        success: function (data) {
            if (data.status != "success") {
                alert("something went wrong!!!")
            }
            else{
                window.location.href = '/short-course-view/';
            }
        }
    });

});


function changePass(){
    otherData = {
        'confPassword':$('#confPassword').val(),
        'newPassword': $('#newPassword').val(),
        'currentPassword':$('#currentPassword').val(),
        'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
    }
   
    $.ajax({
        url: '/password-change/',
        type: "POST",
        contentType : 'application/x-www-form-urlencoded;charset=utf-8',
        data: otherData,
        async : false,
        success: function (data) {
            debugger;
            if (data.sts == false){
                alert(data.msg)
                return false;
            }
            else{
                alert(data.msg)
                window.location.href = '';
            }
        }
    });
}