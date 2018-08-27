var httpobject;

function getRadioVal(name) {
    var radios = document.getElementsByName(name);
    for (var i=0, len=radios.length; i<len; i++) {
        if ( radios[i].checked ) { return radios[i].value; }
    }
}

function getResult() {
    val = getRadioVal("howto");
    httpobject=GetHttpObject();
    httpobject.onreadystatechange=stateChanged;
    if (val=='root') {
        url = 'http://localhost:8100/'
        httpobject.open("GET",url,true); httpobject.send(null);
    }
    if (val=='getOne') {
        paramOne = document.getElementById('paramOne').value;
        paramTwo = document.getElementById('paramTwo').value;
        url = 'http://localhost:8100/funcOne/'+paramOne+'/'+paramTwo+'/';
        httpobject.open("GET",url,true); httpobject.send(null);
    }
    if (val=='postOne') {
        var params = {};
        params.paramOne = document.getElementById('paramOne').value;
        params.paramTwo = document.getElementById('paramTwo').value;
        var json = JSON.stringify(params);
        url = 'http://localhost:8100/funcOne';
        httpobject.open("POST",url,true);
        httpobject.send(json);
    }
    if (val=='getTwo') {
        url = 'http://localhost:8100/funcTwo';
        httpobject.open("GET",url,true); httpobject.send(null);
    }
}

function stateChanged() {
    if (httpobject.readyState==4) {
        document.getElementById("resultDiv").innerHTML=httpobject.responseText;
    }
}

function GetHttpObject() {
        if (window.ActiveXObject) { return new ActiveXObject("Microsoft.XMLHTTP"); } //end if activeXObject
        else {
                    if (window.XMLHttpRequest) { return new XMLHttpRequest();}
                    else {
                                    alert("Your browser does not support AJAX.");
                                    return null;
                                } //end else xmlhttprequest
                } //end else activeXObject
} //end GetHttpObject
