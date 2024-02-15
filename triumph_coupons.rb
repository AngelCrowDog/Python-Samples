def triumph_generate_alphanumeric(prefix,count, slice)
    randoms = Set.new
    while randoms.size < count
      code = Faker::Internet.password(15,5).upcase
      randoms.add("#{code}")
    end

    files = randoms.each_slice(slice).to_a
    i = 1
    files.each do |x|
      name = "generated_data/#{prefix}#{i}.txt"
      File.open(name, "w+") do |f|
        f.puts(x)
      end
      i= i+1
    end
  end