clc
clear

filename = 'thisFileWillRemoveItself.csv';
M = csvread(filename);
input_signal = M(1,2:M(1,1)+1);
kernel = M(2,2:M(2,1)+1);
convolution = conv(input_signal,kernel);
x_inp=0:1:length(input_signal)-1;
x_ker=0:1:length(kernel)-1;
x_conv=0:1:length(convolution)-1;
fig = gcf;
fig.Units = 'inches';
set(fig,'visible','off')
set(fig,'position',[0,0,16,12])
subplot(2,3,1)
y = real(input_signal);
stem(x_inp,y,'square','filled')
title('Input signal (real part)')
xticks(x_inp)
subplot(2,3,2)
y = real(kernel);
stem(x_ker,y,'square','filled')
title('Kernel (real part)')
xticks(x_ker)
subplot(2,3,3)
y = real(convolution);
stem(x_conv,y,'square','filled')
title('Convolution (real part)')
xticks(x_conv)
subplot(2,3,4)
y = imag(input_signal);
stem(x_inp,y,'square','filled')
title('Input signal (imaginary part)')
xticks(x_inp)
subplot(2,3,5)
y = imag(kernel);
stem(x_ker,y,'square','filled')
title('Kernel (imaginary part)')
xticks(x_ker)
subplot(2,3,6)
y = imag(convolution);
stem(x_conv,y,'square','filled')
title('Convolution (imaginary part)')
xticks(x_conv)
saveas(fig,'plotMatlab.png')
delete 'thisFileWillRemoveItself.csv'
