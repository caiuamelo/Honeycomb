function V = DrawHexagonCornerLeft(size,color)

V = zeros(4,2);

Vx = zeros(4,1);
Vy = zeros(4,1);

Vx(1) = 0;
Vy(1) = 0;

Vx(2) = 1*size;
Vy(2) = 0;

Vx(3) = 0.5*size;
Vy(3) = 0.5*sqrt(3)*size;

Vx(4) = 0;
Vy(4) = 0.5*sqrt(3)*size;

%translation = [1.5*(size)*(k-1), mod((k-1),2)*((sqrt(3)/2)*size)...
%    + (l-1)*(size)*sqrt(3)];
translation = [-1*size 0];
Vx = Vx + translation(1);
Vy = Vy + translation(2);

V(:,1) = Vx;
V(:,2) = Vy;

patch(Vx,Vy,color)

end