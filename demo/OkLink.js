function encryptApiKey() {
    var t = 'a2c903cc-b31e-4547-9299-b6d07b7631ab'
        , e = t.split("")
        , n = e.splice(0, 8);
    return t = e.concat(n).join("")
}

function encryptTime(t) {
    var e = (1 * t + 1111111111111).toString().split("")
        , n = parseInt(10 * Math.random(), 10)
        , r = parseInt(10 * Math.random(), 10)
        , o = parseInt(10 * Math.random(), 10);
    return e.concat([n, r, o]).join("")
}

function comb(t, e) {
    var n = "".concat(t, "|").concat(e);
    //btoa--》二进制转base64
    return btoa(n)
}

function getApiKey() {
    var t = (new Date).getTime()
        , e = encryptApiKey();
    return t = encryptTime(t),
        comb(e, t)
}

//加密x-apikey
console.log(getApiKey())