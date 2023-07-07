public class Objeto {
    public String id { get; set; }
    public Integer inicio { get; set; }
    public Integer final { get; set; }
    
    public Objeto(String id, Integer inicio, Integer final) {
        this.id = id;
        this.inicio = inicio;
        this.final = final;
    }
}
