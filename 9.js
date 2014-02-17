var a,b,c;

for (a = 2; a <= 997; a++) {
    for (b = a; b <= 998; b++) {
        c = Math.sqrt( (a * a) + (b * b) )
        if (a+b+c == 1000) {
            console.log(a,b,c,a*b*c);
        }
    }
}