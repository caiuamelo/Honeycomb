function V = DrawHexagonBottom(k,size,color)

V = zeros(4,2);

Vx = zeros(4,1);
Vy = zeros(4,1);

Vx(1) = -0.5*size;
Vy(1) = 0.5*sqrt(3)*size;

Vx(2) = 1.5*size;
Vy(2) = 0.5*sqrt(3)*size;

Vx(3) = 1*size;
Vy(3) = sqrt(3)*size;

Vx(4) = 0;
Vy(4) = sqrt(3)*size;

translation = [k*1.5*size, -0.5*sqrt(3)*size];

Vx = Vx + translation(1);
Vy = Vy + translation(2);

V(:,1) = Vx;
V(:,2) = Vy;

patch(Vx,Vy,color)

end