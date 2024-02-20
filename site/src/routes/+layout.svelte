<script>
    import "../app.css";
  </script>

  <header class='flex justify-center mx-7 bg-gradient-to-b from-slate-100 to-slate-50 rounded-b-xl '>
    <nav class='font-semibold flex justify-between max-w-screen-2xl'>
        <a class='mx-10 text-3xl my-4 hover:bg-slate-200 py-1.5 px-3 rounded-lg' href='./universities'>Universities</a>
        <a class='mx-10 text-3xl my-4 hover:bg-slate-200 py-1.5 px-3 rounded-lg' href='./courses'>Courses</a>
        <a class='mx-10 text-3xl my-4 hover:bg-slate-200 py-1.5 px-3 rounded-lg' href='./modules'>Modules</a>
        <a class='mx-10 text-3xl my-4 hover:bg-slate-200 py-1.5 px-3 rounded-lg' href='./api_access'>API</a>
    </nav>
  </header>
  
  <slot />

  <footer class='bg-gradient-to-t from-slate-100 to-slate-50 rounded-b-xl '>
    <div>
        <h1></h1>
    </div>
  </footer>