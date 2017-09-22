%% La fpp (frontière des possibilités de production)
% Exemple de beurre vs canon de Samuelson
% Cas    A  B  C  D  E  F G
% Beurre 0  1  2  3  4  5 5
% Canon  15 14 12 9  6  9 0

% Données
beurre = [(0:5) 5];
canon = [15 14 12 9 6 9 0];
cas = cellstr(["A", "B", "C", "D", "E", "F", "G"]);
ind = [(1:5) 7];  % valeurs pour la courbe

% Scatter plot
figure;
scatter(beurre, canon)

title("la fpp dans les pays à haut revenu")
xlabel("Beurre (en Mi de kg)")  % Mi = millions
ylabel("Canon (millieres)")
xticks((0:5))
text(beurre + .1, canon, cas);

% Best fit line
hold on
beurre_courbe = beurre(ind);
canon_courbe = canon(ind);
courbe_coeffs = ...
    [beurre_courbe .* beurre_courbe; 
     beurre_courbe;
     ones(size(beurre_courbe))
     ]' \ canon_courbe';
courbe_x = linspace(0, 5);
courbe_y = [courbe_x .* courbe_x; courbe_x; ones(1, 100)]' * courbe_coeffs;
plot(courbe_x, courbe_y, '-')
 