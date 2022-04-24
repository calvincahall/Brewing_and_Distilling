function gravitychart(og)

fg=0.992;
gravity=linspace(og,fg,100);

for i=1:length(gravity);
    abv(i)=((76.08*(og-gravity(i))/(1.775-og))*(gravity(i)/0.794));
end

figure(1)
plot(gravity,abv)
xlabel('Final Gravity')
ylabel('% ABV')

chart=[gravity' abv']

end