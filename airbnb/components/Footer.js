function Footer() {
  return (
    <div className="bg-gray-100 tex-gray-600 ">
      <div className="grid grid-cols-1 md:grid-cols-4 gap-y-14 px-32 py-14 bg-gray-100 tex-gray-600">
        <div className="space-y-4 text-x5 text-gray-800">
          <h5 className="font-bold">ABOUT</h5>
          <p>How Airbnb works</p>
          <p>Newsroom</p>
          <p>Investors</p>
          <p>Airbnb Plus</p>
          <p>Airbnb Luxe</p>
        </div>

        <div className="space-y-4  text-x5 text-gray-800">
          <h5 className="font-bold">COMMUNITY</h5>
          <p>Accessbility</p>
          <p>This is not a real site</p>
          <p>It's awesome clone</p>
          <p>Referal accepted</p>
          <p>Vjdevfam</p>
        </div>

        <div className="space-y-4 text-x5 text-gray-800">
          <h5 className="font-bold">HOST</h5>
          <p>Vjdev React</p>
          <p>Presents</p>
          <p>A full stack clone</p>
          <p>Many applications</p>
          <p>Take a look</p>
        </div>

        <div className="space-y-4 text-x5 text-gray-800">
          <h5 className="font-bold">SUPPORT</h5>
          <p>Help Centre</p>
          <p>Trust & Safety</p>
          <p>Say Hi guys</p>
          <p>Easter Eggs</p>
          <p>For the win</p>
        </div>
      </div>

      <div className="px-32 py-14">
        <div className="border-b  h-1 w-[100%]" />
        <div className=" flex flex-col items-center md:flex md:flex-row md:justify-between text-x5 mt-10 text-gray-800">
          <p>©️ 2021 Airbnb-clone, Inc.</p>
          <p>
            Made by{" "}
            <a
              href="http://vijayraj.netlify.app"
              target="_blank"
              rel="noopener noreferrer"
              className="text-red-400"
            >
              {" "}
              Vijaydev
            </a>{" "}
            with ❤️
          </p>
        </div>
      </div>
    </div>
  );
}

export default Footer;
