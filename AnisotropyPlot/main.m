close all

%% Inputs
numberColunm = 15; % Number of rows
numberRows = 15; % Number od colunm
size = 1; % Size of cell
sigma = 50; % Std of the Normal Distribution

%%
numberColunm = numberColunm - 1;
cellsNumber = length(1:numberRows)*length(1:numberColunm) + ...
    length(1:2:(numberColunm-1)) + ...
    length(0:2:(numberColunm-1)) + ...
    length(0:2:(2*numberRows-1)) + ...
    length(0:numberRows-1) + 2;
    
cord_distrib(cellsNumber,sigma)
distrib =load('distrib.txt');
normDistrib = (distrib + 90)/180;

figure(3)

hold on
ifile = 0;

for i = 1:numberRows
    for j = 1:numberColunm
        ifile = ifile + 1;
        DrawHexagon(i,j,size,normDistrib(ifile))
    end
end

for i = 1:2:(numberColunm-1)
    ifile = ifile + 1;    
    DrawHexagonBottom(i,size,normDistrib(ifile))
end

for i = 0:2:(numberColunm-1)
    ifile = ifile + 1;
    DrawHexagonTop(i,numberRows,size,normDistrib(ifile))
end

for i = 0:2:(2*numberRows-1)
    ifile = ifile + 1;
    DrawHexagonLeft(i,size,normDistrib(ifile))
end


for i = 0:numberRows-1
    ifile = ifile + 1;
    DrawHexagonRight(i,numberColunm,size,normDistrib(ifile))
end


ifile = ifile + 1;
DrawHexagonCornerLeft(size,normDistrib(ifile))

ifile = ifile + 1;
DrawHexagonCornerRight(numberRows,numberColunm,size,normDistrib(ifile))

axis off
axis equal
cbh=colorbar();
colormap 'hot'
caxis([0 1]);
title('Orientation distribution [Degree]')

cbh.TickLabels = {'-90', '-72', '-54', '-36', '-18', '0', '18', '36', ...
    '54', '72', '90'};
