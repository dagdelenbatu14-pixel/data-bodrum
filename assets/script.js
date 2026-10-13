(function () {
  var WA = "905433992863";

  // Kamera ekranı saati
  var clocks = document.querySelectorAll("[data-clock]");
  function pad(n) { return n < 10 ? "0" + n : "" + n; }
  function tick() {
    var d = new Date();
    var t = pad(d.getDate()) + "." + pad(d.getMonth() + 1) + "." + d.getFullYear() + " " +
      pad(d.getHours()) + ":" + pad(d.getMinutes()) + ":" + pad(d.getSeconds());
    for (var i = 0; i < clocks.length; i++) clocks[i].textContent = t;
  }
  if (clocks.length) { tick(); setInterval(tick, 1000); }

  var y = document.querySelectorAll("[data-year]");
  for (var j = 0; j < y.length; j++) y[j].textContent = new Date().getFullYear();

  // Mobil menü: bağlantıya basınca kapan
  var menu = document.querySelector(".menu");
  if (menu) menu.addEventListener("click", function (ev) {
    if (ev.target.closest("a")) menu.removeAttribute("open");
  });

  // Teklif formu → WhatsApp mesajı
  var form = document.getElementById("qf");
  if (!form) return;
  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var ad = form.ad.value.trim(), tel = form.tel.value.trim();
    var err = document.getElementById("qf-err");
    if (!ad || tel.replace(/\D/g, "").length < 10) {
      err.hidden = false;
      (ad ? form.tel : form.ad).focus();
      return;
    }
    err.hidden = true;
    var lines = [
      "Merhaba Data Bodrum, ücretsiz keşif istiyorum.",
      "Ad: " + ad,
      "Telefon: " + tel,
      "Hizmet: " + form.hizmet.value,
      "Bölge: " + form.bolge.value
    ];
    var not = form.not.value.trim();
    if (not) lines.push("Not: " + not);
    window.location.href = "https://wa.me/" + WA + "?text=" + encodeURIComponent(lines.join("\n"));
  });
})();
