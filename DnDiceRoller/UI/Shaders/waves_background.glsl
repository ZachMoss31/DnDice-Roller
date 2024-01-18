---VERTEX SHADER---
#ifdef GL_ES
    precision highp float;
#endif

//https://www.youtube.com/watch?v=CEGz7u3fz4E

varying vec4 frag_color;
varying vec2 text_coord0;

atrribute vec2 vPos;
atrribute vec2 vTextCoords0;

uniform mat4 modelview_mat;
uniform mat4 projection_mat;
uniform vec4 color;
uniform float opacity;

void main (void) {
    frag_color = color * vec4(1.0, 1.0, 1.0, opacity);
    text_coord0 = vTextCoords0;
    gl_Position = projection_mat * modelview_mat * vec4(vPos.xy, 0.0, 1.0);
}

---FRAGMENT SHADER ---

