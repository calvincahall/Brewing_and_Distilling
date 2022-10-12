% Dice for pokemon

doesit=exist('a');

if doesit==0;
    len=1;
    a(len,1)=randi(6);
elseif doesit==1;
    len=length(a);
    a(len+1,1)=randi(6);
end


figure(1)
clf
histogram(a,'numbins',6,'binlimits',[0.5 6.5])
% set(gca)
title('Pokemon Rolls')
xlabel('Number on Die')
ylabel('Frequency of Roll')

figure(2)
clf
track=flipud(a);
plot(track,'-o')
set(gca,'xdir','reverse')
axis([0 length(track) 0 6.5])
