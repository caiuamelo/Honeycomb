function V = DrawHexagonLeft(k,size,color)

V = zeros(5,2);

Vx = zeros(5,1);
Vy = zeros(5,1);

Vx(1) = 0.5;
Vy(1) = 0;

Vx(2) = 1*size;
Vy(2) = 0;

Vx(3) = 1.5*size;
Vy(3) = 0.5*sqrt(3)*size;

Vx(4) = 1*size;
Vy(4) = sqrt(3)*size;

Vx(5) = 0.5*size;
Vy(5) = sqrt(3)*size;

translation = [-1.5*(size), 0.5*(k+1)*sqrt(3)*size];

Vx = Vx + translation(1);
Vy = Vy + translation(2);

V(:,1) = Vx;
V(:,2) = Vy;

patch(Vx,Vy,color)

end