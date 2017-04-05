function V = DrawHexagonCornerRight(nr,nc,size,color)

V = zeros(4,2);

Vx = zeros(4,1);
Vy = zeros(4,1);

if mod(nc,2) == 0
    
    Vx(1) = 0;
    Vy(1) = 0;
    
    Vx(2) = 0.5*size;
    Vy(2) = 0;
    
    Vx(3) = 0.5*size;
    Vy(3) = 0.5*sqrt(3)*size;
    
    Vx(4) = -0.5*size;
    Vy(4) = 0.5*sqrt(3)*size;

    translation = [1.5*(size)*(nc), nr*sqrt(3)*size];
    Vx = Vx + translation(1);
    Vy = Vy + translation(2);    
else
    
    Vx(1) = 0;
    Vy(1) = 0;
    
    Vx(2) = size;
    Vy(2) = 0;
    
    Vx(3) = size;
    Vy(3) = 0.5*sqrt(3)*size;
    
    Vx(4) = 0.5*size;
    Vy(4) = 0.5*sqrt(3)*size;


    translation = [1.5*(size)*(nc) - 0.5*size, 0];
    Vx = Vx + translation(1);
    Vy = Vy + translation(2);
    
end

V(:,1) = Vx;
V(:,2) = Vy;

patch(Vx,Vy,color)

end