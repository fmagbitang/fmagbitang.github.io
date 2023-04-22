let productAmounts = document.getElementsByClassName("pAmount");
let total = document.getElementById("total");
let totalArray = document.querySelectorAll('.total');
let totalamount = 0;

Array.prototype.forEach.call(productAmounts, update);

function update(val, i) {
    val.addEventListener('input', function () {
        var x = val.value;
        let subtotal = (x * document.getElementsByClassName('price')[i].getAttribute("data-amount")).toFixed(3);
        totalArray[i].innerHTML = "$" + subtotal;
        totalUpdate();
    });
};

function totalUpdate() {
    totalamount = 0;
    totalArray.forEach(element => {
        if (element.innerHTML != '0')
            totalamount += parseFloat(element.innerHTML.slice(1));
        else
            totalamount += parseFloat(element.innerHTML.slice(0));
        document.getElementById('total').innerHTML = "$" + totalamount.toFixed(3);
    });
}