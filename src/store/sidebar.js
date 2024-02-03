import { defineStore } from "pinia";

export const useSidebar = defineStore({
  state: () => ({
    menu: [
      {
        name: "Dashboard",
        icon: "",
        type: "default",
        router: true,
        url: "",
      },
      {
        name: "Components",
        icon: "",
        type: "accordion",
        router: true,
        url: false,
        isChildren: true,
        children: [
          {
            name: "Alert",
            icon: false,
            type: "default",
          },
        ],
      },
    ],
  }),
});
