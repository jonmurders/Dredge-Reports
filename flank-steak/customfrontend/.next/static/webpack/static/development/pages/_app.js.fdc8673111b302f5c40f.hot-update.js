webpackHotUpdate("static/development/pages/_app.js",{

/***/ "./node_modules/css-loader/dist/cjs.js?!./node_modules/postcss-loader/src/index.js?!./style.css":
/*!*******************************************************************************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js??ref--5-oneOf-4-1!./node_modules/postcss-loader/src??__nextjs_postcss!./style.css ***!
  \*******************************************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(/*! ./node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js")(true);
// Module
exports.push([module.i, "/* Table of contents\n––––––––––––––––––––––––––––––––––––––––––––––––––\n- Plotly.js\n- Grid\n- Base Styles\n- Typography\n- Links\n- Buttons\n- Forms\n- Lists\n- Code\n- Tables\n- Spacing\n- Utilities\n- Clearing\n- Media Queries\n*/\n\n/* PLotly.js \n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n/* plotly.js's modebar's z-index is 1001 by default\n * https://github.com/plotly/plotly.js/blob/7e4d8ab164258f6bd48be56589dacd9bdd7fded2/src/css/_modebar.scss#L5\n * In case a dropdown is above the graph, the dropdown's options\n * will be rendered below the modebar\n * Increase the select option's z-index\n */\n\n/* This was actually not quite right -\n   dropdowns were overlapping each other (edited October 26)\n\n.Select {\n    z-index: 1002;\n}*/\n\n\n/* Grid\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n.container {\n  position: relative;\n  width: 100%;\n  max-width: 960px;\n  margin: 0 auto;\n  padding: 0 20px;\n  box-sizing: border-box; }\n\n.pretty_container.three.columns {\n  border-radius: 5px;\n  background-color: #f9f9f9;\n  margin: 10px;\n  padding: 15px;\n  position: relative;\n  box-shadow: 2px 2px 2px lightgrey;\n  width: 22%;\n}\n\n.sidebar {\n  height: 100%;\n  width: 160px;\n  position: fixed;\n}\n\n.column,\n.columns {\n  width: 100%;\n  float: left;\n  box-sizing: border-box; }\n\n/* For devices larger than 400px */\n@media (min-width: 400px) {\n  .container {\n    width: 85%;\n    padding: 0; }\n}\n\n/* For devices larger than 550px */\n@media (min-width: 550px) {\n  .container {\n    width: 80%; }\n  .column,\n  .columns {\n    margin-left: 4%; }\n  .column:first-child,\n  .columns:first-child {\n    margin-left: 0; }\n\n  .one.column,\n  .one.columns                    { width: 4.66666666667%; }\n  .two.columns                    { width: 13.3333333333%; }\n  .three.columns                  { width: 22%;            }\n  .four.columns                   { width: 30.6666666667%; }\n  .five.columns                   { width: 39.3333333333%; }\n  .six.columns                    { width: 48%;            }\n  .seven.columns                  { width: 56.6666666667%; }\n  .eight.columns                  { width: 65.3333333333%; }\n  .nine.columns                   { width: 74.0%;          }\n  .ten.columns                    { width: 82.6666666667%; }\n  .eleven.columns                 { width: 91.3333333333%; }\n  .twelve.columns                 { width: 100%; margin-left: 0; }\n\n  .one-third.column               { width: 30.6666666667%; }\n  .two-thirds.column              { width: 65.3333333333%; }\n\n  .one-half.column                { width: 48%; }\n\n  /* Offsets */\n  .offset-by-one.column,\n  .offset-by-one.columns          { margin-left: 8.66666666667%; }\n  .offset-by-two.column,\n  .offset-by-two.columns          { margin-left: 17.3333333333%; }\n  .offset-by-three.column,\n  .offset-by-three.columns        { margin-left: 26%;            }\n  .offset-by-four.column,\n  .offset-by-four.columns         { margin-left: 34.6666666667%; }\n  .offset-by-five.column,\n  .offset-by-five.columns         { margin-left: 43.3333333333%; }\n  .offset-by-six.column,\n  .offset-by-six.columns          { margin-left: 52%;            }\n  .offset-by-seven.column,\n  .offset-by-seven.columns        { margin-left: 60.6666666667%; }\n  .offset-by-eight.column,\n  .offset-by-eight.columns        { margin-left: 69.3333333333%; }\n  .offset-by-nine.column,\n  .offset-by-nine.columns         { margin-left: 78.0%;          }\n  .offset-by-ten.column,\n  .offset-by-ten.columns          { margin-left: 86.6666666667%; }\n  .offset-by-eleven.column,\n  .offset-by-eleven.columns       { margin-left: 95.3333333333%; }\n\n  .offset-by-one-third.column,\n  .offset-by-one-third.columns    { margin-left: 34.6666666667%; }\n  .offset-by-two-thirds.column,\n  .offset-by-two-thirds.columns   { margin-left: 69.3333333333%; }\n\n  .offset-by-one-half.column,\n  .offset-by-one-half.columns     { margin-left: 52%; }\n\n}\n\n\n/* Base Styles\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n/* NOTE\nhtml is set to 62.5% so that all the REM measurements throughout Skeleton\nare based on 10px sizing. So basically 1.5rem = 15px :) */\nhtml {\n  font-size: 62.5%; }\nbody {\n  font-size: 1.5em; /* currently ems cause chrome bug misinterpreting rems on body element */\n  line-height: 1.6;\n  font-weight: 400;\n  font-family: \"Open Sans\", \"HelveticaNeue\", \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n  color: rgb(50, 50, 50); }\n\n\n/* Typography\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\nh1, h2, h3, h4, h5, h6 {\n  margin-top: 0;\n  margin-bottom: 0;\n  font-weight: 300; }\nh1 { font-size: 4.5rem; line-height: 1.2;  letter-spacing: -.1rem; margin-bottom: 2rem; }\nh2 { font-size: 3.6rem; line-height: 1.25; letter-spacing: -.1rem; margin-bottom: 1.8rem; margin-top: 1.8rem;}\nh3 { font-size: 3.0rem; line-height: 1.3;  letter-spacing: -.1rem; margin-bottom: 1.5rem; margin-top: 1.5rem;}\nh4 { font-size: 2.6rem; line-height: 1.35; letter-spacing: -.08rem; margin-bottom: 1.2rem; margin-top: 1.2rem;}\nh5 { font-size: 2.2rem; line-height: 1.5;  letter-spacing: -.05rem; margin-bottom: 0.6rem; margin-top: 0.6rem;}\nh6 { font-size: 2.0rem; line-height: 1.6;  letter-spacing: 0; margin-bottom: 0.75rem; margin-top: 0.75rem;}\n\np {\n  margin-top: 0; }\n\n\n/* Blockquotes\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\nblockquote {\n  border-left: 4px lightgrey solid;\n  padding-left: 1rem;\n  margin-top: 2rem;\n  margin-bottom: 2rem;\n  margin-left: 0rem;\n}\n\n\n/* Links\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\na {\n  color: #1EAEDB; \n  text-decoration: underline;\n  cursor: pointer;}\na:hover {\n  color: #0FA0CE; }\n\n\n/* Buttons\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n.button,\nbutton,\ninput[type=\"submit\"],\ninput[type=\"reset\"],\ninput[type=\"button\"] {\n  display: inline-block;\n  height: 38px;\n  padding: 0 30px;\n  color: #555;\n  text-align: center;\n  font-size: 11px;\n  font-weight: 600;\n  line-height: 38px;\n  letter-spacing: .1rem;\n  text-transform: uppercase;\n  text-decoration: none;\n  white-space: nowrap;\n  background-color: transparent;\n  border-radius: 4px;\n  border: 1px solid #bbb;\n  cursor: pointer;\n  box-sizing: border-box; }\n.button:hover,\nbutton:hover,\ninput[type=\"submit\"]:hover,\ninput[type=\"reset\"]:hover,\ninput[type=\"button\"]:hover,\n.button:focus,\nbutton:focus,\ninput[type=\"submit\"]:focus,\ninput[type=\"reset\"]:focus,\ninput[type=\"button\"]:focus {\n  color: #333;\n  border-color: #888;\n  outline: 0; }\n.button.button-primary,\nbutton.button-primary,\ninput[type=\"submit\"].button-primary,\ninput[type=\"reset\"].button-primary,\ninput[type=\"button\"].button-primary {\n  color: #FFF;\n  background-color: #33C3F0;\n  border-color: #33C3F0; }\n.button.button-primary:hover,\nbutton.button-primary:hover,\ninput[type=\"submit\"].button-primary:hover,\ninput[type=\"reset\"].button-primary:hover,\ninput[type=\"button\"].button-primary:hover,\n.button.button-primary:focus,\nbutton.button-primary:focus,\ninput[type=\"submit\"].button-primary:focus,\ninput[type=\"reset\"].button-primary:focus,\ninput[type=\"button\"].button-primary:focus {\n  color: #FFF;\n  background-color: #1EAEDB;\n  border-color: #1EAEDB; }\n\n\n/* Forms\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\ninput[type=\"email\"],\ninput[type=\"number\"],\ninput[type=\"search\"],\ninput[type=\"text\"],\ninput[type=\"tel\"],\ninput[type=\"url\"],\ninput[type=\"password\"],\ntextarea,\nselect {\n  height: 38px;\n  padding: 6px 10px; /* The 6px vertically centers text on FF, ignored by Webkit */\n  background-color: #fff;\n  border: 1px solid #D1D1D1;\n  border-radius: 4px;\n  box-shadow: none;\n  box-sizing: border-box; \n  font-family: inherit;\n  font-size: inherit; /*https://stackoverflow.com/questions/6080413/why-doesnt-input-inherit-the-font-from-body*/}\n/* Removes awkward default styles on some inputs for iOS */\ninput[type=\"email\"],\ninput[type=\"number\"],\ninput[type=\"search\"],\ninput[type=\"text\"],\ninput[type=\"tel\"],\ninput[type=\"url\"],\ninput[type=\"password\"],\ntextarea {\n  -webkit-appearance: none;\n     -moz-appearance: none;\n          appearance: none; }\ntextarea {\n  min-height: 65px;\n  padding-top: 6px;\n  padding-bottom: 6px; }\ninput[type=\"email\"]:focus,\ninput[type=\"number\"]:focus,\ninput[type=\"search\"]:focus,\ninput[type=\"text\"]:focus,\ninput[type=\"tel\"]:focus,\ninput[type=\"url\"]:focus,\ninput[type=\"password\"]:focus,\ntextarea:focus,\nselect:focus {\n  border: 1px solid #33C3F0;\n  outline: 0; }\nlabel,\nlegend {\n  display: block;\n  margin-bottom: 0px; }\nfieldset {\n  padding: 0;\n  border-width: 0; }\ninput[type=\"checkbox\"],\ninput[type=\"radio\"] {\n  display: inline; }\nlabel > .label-body {\n  display: inline-block;\n  margin-left: .5rem;\n  font-weight: normal; }\n\n\n/* Lists\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\nul {\n  list-style: circle inside; }\nol {\n  list-style: decimal inside; }\nol, ul {\n  padding-left: 0;\n  margin-top: 0; }\nul ul,\nul ol,\nol ol,\nol ul {\n  margin: 1.5rem 0 1.5rem 3rem;\n  font-size: 90%; }\nli {\n  margin-bottom: 1rem; }\n\n\n/* Tables\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\ntable {\n  border-collapse: collapse;\n}\nth:not(.CalendarDay),\ntd:not(.CalendarDay) {\n  padding: 12px 15px;\n  text-align: left;\n  border-bottom: 1px solid #E1E1E1; }\nth:first-child:not(.CalendarDay),\ntd:first-child:not(.CalendarDay) {\n  padding-left: 0; }\nth:last-child:not(.CalendarDay),\ntd:last-child:not(.CalendarDay) {\n  padding-right: 0; }\n\n\n/* Spacing\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\nbutton,\n.button {\n  margin-bottom: 0rem; }\ninput,\ntextarea,\nselect,\nfieldset {\n  margin-bottom: 0rem; }\npre,\ndl,\nfigure,\ntable,\nform {\n  margin-bottom: 0rem; }\np,\nul,\nol {\n  margin-bottom: 0.75rem; }\n\n/* Utilities\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n.u-full-width {\n  width: 100%;\n  box-sizing: border-box; }\n.u-max-full-width {\n  max-width: 100%;\n  box-sizing: border-box; }\n.u-pull-right {\n  float: right; }\n.u-pull-left {\n  float: left; }\n\n\n/* Misc\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\nhr {\n  margin-top: 3rem;\n  margin-bottom: 3.5rem;\n  border-width: 0;\n  border-top: 1px solid #E1E1E1; }\n\n\n/* Clearing\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n\n/* Self Clearing Goodness */\n.container:after,\n.row:after,\n.u-cf {\n  content: \"\";\n  display: table;\n  clear: both; }\n\n\n/* Media Queries\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n/*\nNote: The best way to structure the use of media queries is to create the queries\nnear the relevant code. For example, if you wanted to change the styles for buttons\non small devices, paste the mobile query code up in the buttons section and style it\nthere.\n*/\n\n\n/* Larger than mobile */\n@media (min-width: 400px) {}\n\n/* Larger than phablet (also point when grid becomes active) */\n@media (min-width: 550px) {}\n\n/* Larger than tablet */\n@media (min-width: 750px) {}\n\n/* Larger than desktop */\n@media (min-width: 1000px) {}\n\n/* Larger than Desktop HD */\n@media (min-width: 1200px) {}", "",{"version":3,"sources":["style.css"],"names":[],"mappings":"AAAA;;;;;;;;;;;;;;;;CAgBC;;AAED;oDACoD;AACpD;;;;;EAKE;;AAEF;;;;;EAKE;;;AAGF;oDACoD;AACpD;EACE,kBAAkB;EAClB,WAAW;EACX,gBAAgB;EAChB,cAAc;EACd,eAAe;EACf,sBAAsB,EAAE;;AAE1B;EACE,kBAAkB;EAClB,yBAAyB;EACzB,YAAY;EACZ,aAAa;EACb,kBAAkB;EAClB,iCAAiC;EACjC,UAAU;AACZ;;AAEA;EACE,YAAY;EACZ,YAAY;EACZ,eAAe;AACjB;;AAEA;;EAEE,WAAW;EACX,WAAW;EACX,sBAAsB,EAAE;;AAE1B,kCAAkC;AAClC;EACE;IACE,UAAU;IACV,UAAU,EAAE;AAChB;;AAEA,kCAAkC;AAClC;EACE;IACE,UAAU,EAAE;EACd;;IAEE,eAAe,EAAE;EACnB;;IAEE,cAAc,EAAE;;EAElB;oCACkC,qBAAqB,EAAE;EACzD,kCAAkC,qBAAqB,EAAE;EACzD,kCAAkC,UAAU,aAAa;EACzD,kCAAkC,qBAAqB,EAAE;EACzD,kCAAkC,qBAAqB,EAAE;EACzD,kCAAkC,UAAU,aAAa;EACzD,kCAAkC,qBAAqB,EAAE;EACzD,kCAAkC,qBAAqB,EAAE;EACzD,kCAAkC,YAAY,WAAW;EACzD,kCAAkC,qBAAqB,EAAE;EACzD,kCAAkC,qBAAqB,EAAE;EACzD,kCAAkC,WAAW,EAAE,cAAc,EAAE;;EAE/D,kCAAkC,qBAAqB,EAAE;EACzD,kCAAkC,qBAAqB,EAAE;;EAEzD,kCAAkC,UAAU,EAAE;;EAE9C,YAAY;EACZ;oCACkC,2BAA2B,EAAE;EAC/D;oCACkC,2BAA2B,EAAE;EAC/D;oCACkC,gBAAgB,aAAa;EAC/D;oCACkC,2BAA2B,EAAE;EAC/D;oCACkC,2BAA2B,EAAE;EAC/D;oCACkC,gBAAgB,aAAa;EAC/D;oCACkC,2BAA2B,EAAE;EAC/D;oCACkC,2BAA2B,EAAE;EAC/D;oCACkC,kBAAkB,WAAW;EAC/D;oCACkC,2BAA2B,EAAE;EAC/D;oCACkC,2BAA2B,EAAE;;EAE/D;oCACkC,2BAA2B,EAAE;EAC/D;oCACkC,2BAA2B,EAAE;;EAE/D;oCACkC,gBAAgB,EAAE;;AAEtD;;;AAGA;oDACoD;AACpD;;yDAEyD;AACzD;EACE,gBAAgB,EAAE;AACpB;EACE,gBAAgB,EAAE,wEAAwE;EAC1F,gBAAgB;EAChB,gBAAgB;EAChB,yFAAyF;EACzF,sBAAsB,EAAE;;;AAG1B;oDACoD;AACpD;EACE,aAAa;EACb,gBAAgB;EAChB,gBAAgB,EAAE;AACpB,KAAK,iBAAiB,EAAE,gBAAgB,GAAG,sBAAsB,EAAE,mBAAmB,EAAE;AACxF,KAAK,iBAAiB,EAAE,iBAAiB,EAAE,sBAAsB,EAAE,qBAAqB,EAAE,kBAAkB,CAAC;AAC7G,KAAK,iBAAiB,EAAE,gBAAgB,GAAG,sBAAsB,EAAE,qBAAqB,EAAE,kBAAkB,CAAC;AAC7G,KAAK,iBAAiB,EAAE,iBAAiB,EAAE,uBAAuB,EAAE,qBAAqB,EAAE,kBAAkB,CAAC;AAC9G,KAAK,iBAAiB,EAAE,gBAAgB,GAAG,uBAAuB,EAAE,qBAAqB,EAAE,kBAAkB,CAAC;AAC9G,KAAK,iBAAiB,EAAE,gBAAgB,GAAG,iBAAiB,EAAE,sBAAsB,EAAE,mBAAmB,CAAC;;AAE1G;EACE,aAAa,EAAE;;;AAGjB;oDACoD;AACpD;EACE,gCAAgC;EAChC,kBAAkB;EAClB,gBAAgB;EAChB,mBAAmB;EACnB,iBAAiB;AACnB;;;AAGA;oDACoD;AACpD;EACE,cAAc;EACd,0BAA0B;EAC1B,eAAe,CAAC;AAClB;EACE,cAAc,EAAE;;;AAGlB;oDACoD;AACpD;;;;;EAKE,qBAAqB;EACrB,YAAY;EACZ,eAAe;EACf,WAAW;EACX,kBAAkB;EAClB,eAAe;EACf,gBAAgB;EAChB,iBAAiB;EACjB,qBAAqB;EACrB,yBAAyB;EACzB,qBAAqB;EACrB,mBAAmB;EACnB,6BAA6B;EAC7B,kBAAkB;EAClB,sBAAsB;EACtB,eAAe;EACf,sBAAsB,EAAE;AAC1B;;;;;;;;;;EAUE,WAAW;EACX,kBAAkB;EAClB,UAAU,EAAE;AACd;;;;;EAKE,WAAW;EACX,yBAAyB;EACzB,qBAAqB,EAAE;AACzB;;;;;;;;;;EAUE,WAAW;EACX,yBAAyB;EACzB,qBAAqB,EAAE;;;AAGzB;oDACoD;AACpD;;;;;;;;;EASE,YAAY;EACZ,iBAAiB,EAAE,6DAA6D;EAChF,sBAAsB;EACtB,yBAAyB;EACzB,kBAAkB;EAClB,gBAAgB;EAChB,sBAAsB;EACtB,oBAAoB;EACpB,kBAAkB,EAAE,0FAA0F,CAAC;AACjH,0DAA0D;AAC1D;;;;;;;;EAQE,wBAAwB;KACrB,qBAAqB;UAChB,gBAAgB,EAAE;AAC5B;EACE,gBAAgB;EAChB,gBAAgB;EAChB,mBAAmB,EAAE;AACvB;;;;;;;;;EASE,yBAAyB;EACzB,UAAU,EAAE;AACd;;EAEE,cAAc;EACd,kBAAkB,EAAE;AACtB;EACE,UAAU;EACV,eAAe,EAAE;AACnB;;EAEE,eAAe,EAAE;AACnB;EACE,qBAAqB;EACrB,kBAAkB;EAClB,mBAAmB,EAAE;;;AAGvB;oDACoD;AACpD;EACE,yBAAyB,EAAE;AAC7B;EACE,0BAA0B,EAAE;AAC9B;EACE,eAAe;EACf,aAAa,EAAE;AACjB;;;;EAIE,4BAA4B;EAC5B,cAAc,EAAE;AAClB;EACE,mBAAmB,EAAE;;;AAGvB;oDACoD;AACpD;EACE,yBAAyB;AAC3B;AACA;;EAEE,kBAAkB;EAClB,gBAAgB;EAChB,gCAAgC,EAAE;AACpC;;EAEE,eAAe,EAAE;AACnB;;EAEE,gBAAgB,EAAE;;;AAGpB;oDACoD;AACpD;;EAEE,mBAAmB,EAAE;AACvB;;;;EAIE,mBAAmB,EAAE;AACvB;;;;;EAKE,mBAAmB,EAAE;AACvB;;;EAGE,sBAAsB,EAAE;;AAE1B;oDACoD;AACpD;EACE,WAAW;EACX,sBAAsB,EAAE;AAC1B;EACE,eAAe;EACf,sBAAsB,EAAE;AAC1B;EACE,YAAY,EAAE;AAChB;EACE,WAAW,EAAE;;;AAGf;oDACoD;AACpD;EACE,gBAAgB;EAChB,qBAAqB;EACrB,eAAe;EACf,6BAA6B,EAAE;;;AAGjC;oDACoD;;AAEpD,2BAA2B;AAC3B;;;EAGE,WAAW;EACX,cAAc;EACd,WAAW,EAAE;;;AAGf;oDACoD;AACpD;;;;;CAKC;;;AAGD,uBAAuB;AACvB,2BAA2B;;AAE3B,8DAA8D;AAC9D,2BAA2B;;AAE3B,uBAAuB;AACvB,2BAA2B;;AAE3B,wBAAwB;AACxB,4BAA4B;;AAE5B,2BAA2B;AAC3B,4BAA4B","file":"style.css","sourcesContent":["/* Table of contents\n––––––––––––––––––––––––––––––––––––––––––––––––––\n- Plotly.js\n- Grid\n- Base Styles\n- Typography\n- Links\n- Buttons\n- Forms\n- Lists\n- Code\n- Tables\n- Spacing\n- Utilities\n- Clearing\n- Media Queries\n*/\n\n/* PLotly.js \n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n/* plotly.js's modebar's z-index is 1001 by default\n * https://github.com/plotly/plotly.js/blob/7e4d8ab164258f6bd48be56589dacd9bdd7fded2/src/css/_modebar.scss#L5\n * In case a dropdown is above the graph, the dropdown's options\n * will be rendered below the modebar\n * Increase the select option's z-index\n */\n\n/* This was actually not quite right -\n   dropdowns were overlapping each other (edited October 26)\n\n.Select {\n    z-index: 1002;\n}*/\n\n\n/* Grid\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n.container {\n  position: relative;\n  width: 100%;\n  max-width: 960px;\n  margin: 0 auto;\n  padding: 0 20px;\n  box-sizing: border-box; }\n\n.pretty_container.three.columns {\n  border-radius: 5px;\n  background-color: #f9f9f9;\n  margin: 10px;\n  padding: 15px;\n  position: relative;\n  box-shadow: 2px 2px 2px lightgrey;\n  width: 22%;\n}\n\n.sidebar {\n  height: 100%;\n  width: 160px;\n  position: fixed;\n}\n\n.column,\n.columns {\n  width: 100%;\n  float: left;\n  box-sizing: border-box; }\n\n/* For devices larger than 400px */\n@media (min-width: 400px) {\n  .container {\n    width: 85%;\n    padding: 0; }\n}\n\n/* For devices larger than 550px */\n@media (min-width: 550px) {\n  .container {\n    width: 80%; }\n  .column,\n  .columns {\n    margin-left: 4%; }\n  .column:first-child,\n  .columns:first-child {\n    margin-left: 0; }\n\n  .one.column,\n  .one.columns                    { width: 4.66666666667%; }\n  .two.columns                    { width: 13.3333333333%; }\n  .three.columns                  { width: 22%;            }\n  .four.columns                   { width: 30.6666666667%; }\n  .five.columns                   { width: 39.3333333333%; }\n  .six.columns                    { width: 48%;            }\n  .seven.columns                  { width: 56.6666666667%; }\n  .eight.columns                  { width: 65.3333333333%; }\n  .nine.columns                   { width: 74.0%;          }\n  .ten.columns                    { width: 82.6666666667%; }\n  .eleven.columns                 { width: 91.3333333333%; }\n  .twelve.columns                 { width: 100%; margin-left: 0; }\n\n  .one-third.column               { width: 30.6666666667%; }\n  .two-thirds.column              { width: 65.3333333333%; }\n\n  .one-half.column                { width: 48%; }\n\n  /* Offsets */\n  .offset-by-one.column,\n  .offset-by-one.columns          { margin-left: 8.66666666667%; }\n  .offset-by-two.column,\n  .offset-by-two.columns          { margin-left: 17.3333333333%; }\n  .offset-by-three.column,\n  .offset-by-three.columns        { margin-left: 26%;            }\n  .offset-by-four.column,\n  .offset-by-four.columns         { margin-left: 34.6666666667%; }\n  .offset-by-five.column,\n  .offset-by-five.columns         { margin-left: 43.3333333333%; }\n  .offset-by-six.column,\n  .offset-by-six.columns          { margin-left: 52%;            }\n  .offset-by-seven.column,\n  .offset-by-seven.columns        { margin-left: 60.6666666667%; }\n  .offset-by-eight.column,\n  .offset-by-eight.columns        { margin-left: 69.3333333333%; }\n  .offset-by-nine.column,\n  .offset-by-nine.columns         { margin-left: 78.0%;          }\n  .offset-by-ten.column,\n  .offset-by-ten.columns          { margin-left: 86.6666666667%; }\n  .offset-by-eleven.column,\n  .offset-by-eleven.columns       { margin-left: 95.3333333333%; }\n\n  .offset-by-one-third.column,\n  .offset-by-one-third.columns    { margin-left: 34.6666666667%; }\n  .offset-by-two-thirds.column,\n  .offset-by-two-thirds.columns   { margin-left: 69.3333333333%; }\n\n  .offset-by-one-half.column,\n  .offset-by-one-half.columns     { margin-left: 52%; }\n\n}\n\n\n/* Base Styles\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n/* NOTE\nhtml is set to 62.5% so that all the REM measurements throughout Skeleton\nare based on 10px sizing. So basically 1.5rem = 15px :) */\nhtml {\n  font-size: 62.5%; }\nbody {\n  font-size: 1.5em; /* currently ems cause chrome bug misinterpreting rems on body element */\n  line-height: 1.6;\n  font-weight: 400;\n  font-family: \"Open Sans\", \"HelveticaNeue\", \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n  color: rgb(50, 50, 50); }\n\n\n/* Typography\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\nh1, h2, h3, h4, h5, h6 {\n  margin-top: 0;\n  margin-bottom: 0;\n  font-weight: 300; }\nh1 { font-size: 4.5rem; line-height: 1.2;  letter-spacing: -.1rem; margin-bottom: 2rem; }\nh2 { font-size: 3.6rem; line-height: 1.25; letter-spacing: -.1rem; margin-bottom: 1.8rem; margin-top: 1.8rem;}\nh3 { font-size: 3.0rem; line-height: 1.3;  letter-spacing: -.1rem; margin-bottom: 1.5rem; margin-top: 1.5rem;}\nh4 { font-size: 2.6rem; line-height: 1.35; letter-spacing: -.08rem; margin-bottom: 1.2rem; margin-top: 1.2rem;}\nh5 { font-size: 2.2rem; line-height: 1.5;  letter-spacing: -.05rem; margin-bottom: 0.6rem; margin-top: 0.6rem;}\nh6 { font-size: 2.0rem; line-height: 1.6;  letter-spacing: 0; margin-bottom: 0.75rem; margin-top: 0.75rem;}\n\np {\n  margin-top: 0; }\n\n\n/* Blockquotes\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\nblockquote {\n  border-left: 4px lightgrey solid;\n  padding-left: 1rem;\n  margin-top: 2rem;\n  margin-bottom: 2rem;\n  margin-left: 0rem;\n}\n\n\n/* Links\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\na {\n  color: #1EAEDB; \n  text-decoration: underline;\n  cursor: pointer;}\na:hover {\n  color: #0FA0CE; }\n\n\n/* Buttons\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n.button,\nbutton,\ninput[type=\"submit\"],\ninput[type=\"reset\"],\ninput[type=\"button\"] {\n  display: inline-block;\n  height: 38px;\n  padding: 0 30px;\n  color: #555;\n  text-align: center;\n  font-size: 11px;\n  font-weight: 600;\n  line-height: 38px;\n  letter-spacing: .1rem;\n  text-transform: uppercase;\n  text-decoration: none;\n  white-space: nowrap;\n  background-color: transparent;\n  border-radius: 4px;\n  border: 1px solid #bbb;\n  cursor: pointer;\n  box-sizing: border-box; }\n.button:hover,\nbutton:hover,\ninput[type=\"submit\"]:hover,\ninput[type=\"reset\"]:hover,\ninput[type=\"button\"]:hover,\n.button:focus,\nbutton:focus,\ninput[type=\"submit\"]:focus,\ninput[type=\"reset\"]:focus,\ninput[type=\"button\"]:focus {\n  color: #333;\n  border-color: #888;\n  outline: 0; }\n.button.button-primary,\nbutton.button-primary,\ninput[type=\"submit\"].button-primary,\ninput[type=\"reset\"].button-primary,\ninput[type=\"button\"].button-primary {\n  color: #FFF;\n  background-color: #33C3F0;\n  border-color: #33C3F0; }\n.button.button-primary:hover,\nbutton.button-primary:hover,\ninput[type=\"submit\"].button-primary:hover,\ninput[type=\"reset\"].button-primary:hover,\ninput[type=\"button\"].button-primary:hover,\n.button.button-primary:focus,\nbutton.button-primary:focus,\ninput[type=\"submit\"].button-primary:focus,\ninput[type=\"reset\"].button-primary:focus,\ninput[type=\"button\"].button-primary:focus {\n  color: #FFF;\n  background-color: #1EAEDB;\n  border-color: #1EAEDB; }\n\n\n/* Forms\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\ninput[type=\"email\"],\ninput[type=\"number\"],\ninput[type=\"search\"],\ninput[type=\"text\"],\ninput[type=\"tel\"],\ninput[type=\"url\"],\ninput[type=\"password\"],\ntextarea,\nselect {\n  height: 38px;\n  padding: 6px 10px; /* The 6px vertically centers text on FF, ignored by Webkit */\n  background-color: #fff;\n  border: 1px solid #D1D1D1;\n  border-radius: 4px;\n  box-shadow: none;\n  box-sizing: border-box; \n  font-family: inherit;\n  font-size: inherit; /*https://stackoverflow.com/questions/6080413/why-doesnt-input-inherit-the-font-from-body*/}\n/* Removes awkward default styles on some inputs for iOS */\ninput[type=\"email\"],\ninput[type=\"number\"],\ninput[type=\"search\"],\ninput[type=\"text\"],\ninput[type=\"tel\"],\ninput[type=\"url\"],\ninput[type=\"password\"],\ntextarea {\n  -webkit-appearance: none;\n     -moz-appearance: none;\n          appearance: none; }\ntextarea {\n  min-height: 65px;\n  padding-top: 6px;\n  padding-bottom: 6px; }\ninput[type=\"email\"]:focus,\ninput[type=\"number\"]:focus,\ninput[type=\"search\"]:focus,\ninput[type=\"text\"]:focus,\ninput[type=\"tel\"]:focus,\ninput[type=\"url\"]:focus,\ninput[type=\"password\"]:focus,\ntextarea:focus,\nselect:focus {\n  border: 1px solid #33C3F0;\n  outline: 0; }\nlabel,\nlegend {\n  display: block;\n  margin-bottom: 0px; }\nfieldset {\n  padding: 0;\n  border-width: 0; }\ninput[type=\"checkbox\"],\ninput[type=\"radio\"] {\n  display: inline; }\nlabel > .label-body {\n  display: inline-block;\n  margin-left: .5rem;\n  font-weight: normal; }\n\n\n/* Lists\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\nul {\n  list-style: circle inside; }\nol {\n  list-style: decimal inside; }\nol, ul {\n  padding-left: 0;\n  margin-top: 0; }\nul ul,\nul ol,\nol ol,\nol ul {\n  margin: 1.5rem 0 1.5rem 3rem;\n  font-size: 90%; }\nli {\n  margin-bottom: 1rem; }\n\n\n/* Tables\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\ntable {\n  border-collapse: collapse;\n}\nth:not(.CalendarDay),\ntd:not(.CalendarDay) {\n  padding: 12px 15px;\n  text-align: left;\n  border-bottom: 1px solid #E1E1E1; }\nth:first-child:not(.CalendarDay),\ntd:first-child:not(.CalendarDay) {\n  padding-left: 0; }\nth:last-child:not(.CalendarDay),\ntd:last-child:not(.CalendarDay) {\n  padding-right: 0; }\n\n\n/* Spacing\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\nbutton,\n.button {\n  margin-bottom: 0rem; }\ninput,\ntextarea,\nselect,\nfieldset {\n  margin-bottom: 0rem; }\npre,\ndl,\nfigure,\ntable,\nform {\n  margin-bottom: 0rem; }\np,\nul,\nol {\n  margin-bottom: 0.75rem; }\n\n/* Utilities\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n.u-full-width {\n  width: 100%;\n  box-sizing: border-box; }\n.u-max-full-width {\n  max-width: 100%;\n  box-sizing: border-box; }\n.u-pull-right {\n  float: right; }\n.u-pull-left {\n  float: left; }\n\n\n/* Misc\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\nhr {\n  margin-top: 3rem;\n  margin-bottom: 3.5rem;\n  border-width: 0;\n  border-top: 1px solid #E1E1E1; }\n\n\n/* Clearing\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n\n/* Self Clearing Goodness */\n.container:after,\n.row:after,\n.u-cf {\n  content: \"\";\n  display: table;\n  clear: both; }\n\n\n/* Media Queries\n–––––––––––––––––––––––––––––––––––––––––––––––––– */\n/*\nNote: The best way to structure the use of media queries is to create the queries\nnear the relevant code. For example, if you wanted to change the styles for buttons\non small devices, paste the mobile query code up in the buttons section and style it\nthere.\n*/\n\n\n/* Larger than mobile */\n@media (min-width: 400px) {}\n\n/* Larger than phablet (also point when grid becomes active) */\n@media (min-width: 550px) {}\n\n/* Larger than tablet */\n@media (min-width: 750px) {}\n\n/* Larger than desktop */\n@media (min-width: 1000px) {}\n\n/* Larger than Desktop HD */\n@media (min-width: 1200px) {}"]}]);


/***/ })

})
//# sourceMappingURL=_app.js.fdc8673111b302f5c40f.hot-update.js.map