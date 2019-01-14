window.onload = function () {


document.getElementById('addButton').onclick = function () {
    document.getElementById('toAdd').style.display = 'block';
    document.getElementsByClassName('addDiv')[0].style.display = 'none';
    document.getElementById('dropCheck').style.display = 'block';


}

document.getElementById('drop').onclick = function () {
    document.getElementById('toAdd').style.display = 'none';
    document.getElementsByClassName('addDiv')[0].style.display = 'block';
    document.getElementById('dropCheck').style.display = 'none';
}

};