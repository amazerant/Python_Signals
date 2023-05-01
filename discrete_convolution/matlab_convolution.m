clc

FILE_PATH = '';

u = 1000*rand(1,100000)' + 1000j*rand(1,100000)';
v = 1000*rand(1,100000)' + 1000j*rand(1,100000)';
w = conv(u,v);
U = size(w)-size(u);
V = size(w)-size(v);
matrix = [[u ; NaN(U(1),1)] [v ; NaN(V(1),1)] w];

csvwrite(FILE_PATH,matrix);



