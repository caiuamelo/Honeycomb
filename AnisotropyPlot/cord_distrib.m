function cord_distrib(z,sigma)
%% Normal Distribution Honeycomb Orientation
%z = 121; % Number of honeycomb cells

bot_bound = -90; % Bottom Boundary of the Normal Distribution
upp_bound = 90; % Upper Boundary of the Normal Distribution

mu = 0; % Mean of the Normal Distribution
%sigma = 40; % Std of the Normal Distribution

pd=makedist('Normal','mu',mu,'sigma',sigma);
distrib=random(pd,z,1);

figure(1)
hist(distrib,[-90 -75 -60 -45 -30 -15 0 15 30 45 60 75 90])
xlabel('Cell Orientation [Degree]')
ylabel('Number of Cells with this Orientation')
xlim([-90 90])

[counts,centers] = hist(distrib,[-90 -75 -60 -45 -30 -15 0 15 30 45 60 75 90]);

figure(2)
subplot(2,1,1)
bar(centers,counts)
ylabel('Number of Cells with this Orientation')
xlabel('Cell Orientation [Degree]')
subplot(2,1,2)
bar(distrib)
ylabel('Cell Orientation [Degree]')
xlabel('Cell Number')
ylim([-90 90])
xlim([0 z])

save('distrib.txt','distrib','-ascii')
