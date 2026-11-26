/* Fill the footer's "last updated" line from the page's Last-Modified date.
   GitHub Pages sets Last-Modified to the deploy time, so this needs no manual edits. */
(function () {
   var el = document.getElementById('last-updated');
   if (!el) {
      return;
   }
   var d = new Date(document.lastModified);
   var t = d.getTime();
   if (isNaN(t) || t <= 0) {
      return;
   }
   var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
      'August', 'September', 'October', 'November', 'December'];
   el.textContent = 'Site last updated: ' + months[d.getMonth()] + ' ' + d.getDate() + ', ' + d.getFullYear();
})();
