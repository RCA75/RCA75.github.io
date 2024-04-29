"use strict";(self["webpackChunk_31_tienda_de_juegos_32bits"]=self["webpackChunk_31_tienda_de_juegos_32bits"]||[]).push([[643],{3643:function(e,o,t){t.r(o),t.d(o,{default:function(){return A}});var l=function(){var e=this,o=e.$createElement,t=e._self._c||o;return t("div",[t("h1",[e._v("Vista de Juegos")]),t("JuegosCarousel"),t("hr"),t("h4",[e._v("Lista de Juegos")]),t("JuegosTabla")],1)},n=[],r=t(7875),u=function(){var e=this,o=e.$createElement,t=e._self._c||o;return t("div",[e.loadingJuegos?t("LottieAnimation",{ref:"anim",attrs:{path:"./loading.json"}}):e._e(),e.loadingJuegos?e._e():t("carousel-3d",e._l(e.juegos,(function(e,o){return t("slide",{key:o,attrs:{index:o}},[t("img",{attrs:{src:e.cover,alt:""}})])})),1)],1)},a=[],s=t(8767),c=t(4665),i={components:{LottieAnimation:s.Z},computed:{...(0,c.rn)("juegos",{juegos:e=>e.listado,loadingJuegos:e=>e.loading})}},_=i,g=t(1001),d=(0,g.Z)(_,u,a,!1,null,null,null),v=d.exports,b=function(){var e=this,o=e.$createElement,t=e._self._c||o;return t("table",{staticClass:"table"},[e._m(0),t("tbody",e._l(e.juegos,(function(o,l){return t("tr",{key:l,style:{color:o.color}},[t("td",[e._v(e._s(o.codigo))]),t("td",[t("select",{domProps:{value:o.color},on:{change:function(t){return e.cambiarColorAUnJuego(o,t)}}},e._l(e.colores,(function(o,l){return t("option",{key:l,domProps:{value:o.value}},[e._v(" "+e._s(o.label)+" ")])})),0)]),t("td",[e._v(e._s(o.nombre))]),t("td",[e._v(e._s(o.stock))]),t("td",[e._v(e._s(o.precio))]),t("td",[t("button",{on:{click:function(t){return e.agregarStock(o)}}},[e._v("+")]),t("button",{on:{click:function(t){return e.quitarStock(o)}}},[e._v("-")])])])})),0)])},h=[function(){var e=this,o=e.$createElement,t=e._self._c||o;return t("thead",[t("tr",[t("th",[e._v("Código")]),t("th",[e._v("Color")]),t("th",[e._v("Nombre")]),t("th",[e._v("Stock")]),t("th",[e._v("Precio")]),t("th",[e._v("Acciones")])])])}],m={data:()=>({colores:[{value:"red",label:"Rojo"},{value:"blue",label:"Azul"},{value:"green",label:"Verde"},{value:"black",label:"Negro"}]}),computed:{...(0,c.rn)("juegos",{juegos:e=>e.listado})},methods:{...(0,c.nv)("juegos",["agregarStock","quitarStock","cambiarColor"]),cambiarColorAUnJuego(e,o){this.cambiarColor({juegoABuscar:e,nuevoColor:o.target.value})}}},f=m,k=(0,g.Z)(f,b,h,!1,null,null,null),p=k.exports,j={components:{JuegosCarousel:v,JuegosTabla:p},beforeRouteEnter(e,o,t){r.Z.dispatch("juegos/getAllJuegos"),t()}},C=j,J=(0,g.Z)(C,l,n,!1,null,null,null),A=J.exports}}]);
//# sourceMappingURL=643.69d5c15f.js.map 