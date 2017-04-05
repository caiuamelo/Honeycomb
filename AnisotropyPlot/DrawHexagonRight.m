function V = DrawHexagonRight(l,nc,size,color)

V = zeros(5,2);

Vx = zeros(5,1);
Vy = zeros(5,1);

Vx(1) = 0;
Vy(1) = 0;

Vx(2) = 0.5*size;
Vy(2) = 0;

Vx(3) = 0.5*size;
Vy(3) = sqrt(3)*size;

Vx(4) = 0;
Vy(4) = sqrt(3)*size;

Vx(5) = -0.5;
Vy(5) = 0.5*sqrt(3)*size;

translation = [1.5*(size)*(nc), mod((nc),2)*((sqrt(3)/2)*size)...
    + (l)*(size)*sqrt(3)];
Vx = Vx + translation(1);
Vy = Vy + translation(2);

V(:,1) = Vx;
V(:,2) = Vy;

patch(Vx,Vy,color)

end